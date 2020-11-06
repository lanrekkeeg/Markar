
from app.util.util import *
from app.configuration.config import *
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

class DB:
    def __init__(self, name=None,logging=None,email=None, token=None,request_data=None, user_type=None):
        self.log = logging
        self.token = token
        self.payload  = request_data
        self.user_type = user_type
        self.db_con = self.create_connection()
        self.email = email
        self.name = name


    def close_connection(self):
        """
        will close the connection beforehand
        """
    def create_connection(self):
        """
        it will create database base on configuration value
        """
        self.log.debug("creating connection")
        try:
            db_con = mysql.connector.connect(user=USER,password=PASS,host=MysqlAddress,
                                        database=DBName)
        except mysql.connector.Error as err:
            self.log.debug("Erro")
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.log.info("Created successfully")
            return db_con
            #return "successfully establish connection"
            
    def validate_admin(self):
        """
        validate wheather particular person is admin or not
        """

        cursor = self.db_con.cursor()
        if self.user_type == "STUDENTS":
            query = ("SELECT * FROM "+self.user_type+
            " WHERE EMAIL=%s and TOKEN=%s")
            self.log.debug("Query:{}".format(query))
            cursor.execute(query, (self.payload['email'],self.payload['token']))
        elif self.user_type == "ADMIN":
            query = ("SELECT * FROM "+self.user_type+
            " WHERE EMAIL=%s and TOKEN=%s")
            self.log.debug("Query:{}".format(query))
            cursor.execute(query, (self.email,self.token))
        res = cursor.fetchone()
        self.log.debug("Result from validate {} table {}".format(self.user_type,res))
        if res is None:
            return False
        else:
            return True
    
    def add_admin():
        """
        Adding new admin
        """
        self.validate_admin()

        # validate admin

    def register_user(self):
        """
        Adding new user to db
        """
        self.log.debug("Inside register user function")
        if self.check_user_exist() == False:
            self.log.debug("check is pass")
            return "User already exist"
        self.log.debug("check is pass")
        token = generate_token()
        #email = convert_into_email(self.EMAIL)
        add_students = ("INSERT INTO STUDENTS "
               "(STUDENT_NAME, EMAIL, TOKEN) "
               "VALUES (%s, %s, %s)")
        self.log.debug("rollNo:{},email:{},token:{}".format(self.payload['name'], self.payload['email'], str(token)))
        student_data = (self.payload['name'], self.payload['email'], str(token))
        cursor = self.db_con.cursor()
        cursor.execute(add_students, student_data)
        self.db_con.commit()
        message = "Hi {0},\n  Your token to access Markar is stated below\n  Token: {1}\n\nPlease make sure you don't ever share this token with anybody for security purposes. Do not delete this email as this token will remain the same throughout this semester. Use your NU mail id and this token to log in to Markar.\nIf somebody gets access to your account on Markar and does something undesirable, I will simply ignore all excuses or reasons.\n\nRegards,\nFaisal khan"\
            .format(self.payload['name'], token)
        send_mail("faisal.khan@nu.edu.pk",self.email,message, "Markar Registration Alert")
        return "Student register"

    def check_user_exist(self):
        """
        checking if user already exist
        """
        self.log.debug("Checking user existence in autograder table")
        cursor = self.db_con.cursor()
        query = ("SELECT * FROM STUDENTS"
         " WHERE EMAIL=%s")
        self.log.debug("Query:{}".format(query))
        cursor.execute(query, (self.payload['email'],))
        res = cursor.fetchone()
        self.log.debug("Result from students table {}".format(res))
        if res is None:
            return True
        else:
            return False
        
    def check_course_code_exist(self):
        """
        checking if course code already exist
        """
        code_name = self.payload['coursecode']
        cursor = self.db_con.cursor()
        query = ("SELECT * FROM CODES_LIST"
         " WHERE CODE=%s")
        cursor.execute(query, (code_name,))
        res = cursor.fetchone()
        self.log.debug("Result from Codes_List table {}".format(res))
        if res is None:
            return True
        else:
            return False

    def verify_coure_base_registration(self):
        """
        check if student is registered to lab or course  for task submission

        Note: This function will be merged with check_student_registration
        """
        code_name = self.payload['coursecode']
        email = self.payload['email']
        
        if self.payload['type'] == "Task":
            section = self.payload['section']
            cursor = self.db_con.cursor()
            self.log.debug("checking the student in the course in student list: {},{}".format(code_name,email))
            query = ("SELECT * FROM STUDENTS_LIST"
            " WHERE CODE=%s AND EMAIL=%s AND SECTION=%s")
            cursor.execute(query, (code_name,email, section))
            res = cursor.fetchone()
            self.log.debug("Result from Courses table {}".format(res))
            if res is None:
                return True
            else:
                return False
        else:
            return check_student_registeration()

    def check_student_registeration(self):
        """
        check if student is registeter in any course
        """
        
        code_name = self.payload['coursecode']
        email = self.payload['email']
            
        # WE NEED TO ADD SECTION
        #section = self.payload['section']
        cursor = self.db_con.cursor()
        self.log.debug("checking the student in the course in student list: {},{}".format(code_name,email))
        query = ("SELECT * FROM STUDENTS_LIST"
         " WHERE CODE=%s AND EMAIL=%s")
        cursor.execute(query, (code_name,email))
        res = cursor.fetchone()
        self.log.debug("Result from Courses table {}".format(res))
        if res is None:
            return True
        else:
            return False


    def add_course_code(self):
        """
        checking if user already exist
        """
        if self.check_course_code_exist() == False:
            self.log.debug("check is pass")
            return "Code already exist"

        add_course = ("INSERT INTO CODES_LIST "
               "(NAME,CODE) "
               "VALUES (%s, %s)")
        self.log.debug("name:{},code:{}".format(self.payload['name'], self.payload['coursecode']))
        course_data = (self.payload['name'], self.payload['coursecode'])
        cursor = self.db_con.cursor()
        cursor.execute(add_course, course_data)
        self.db_con.commit()
    
        #send_mail("faisal.khan@nu.edu.pk",self.email,"Your secured token for login is "+str(token))
        return "Course Added, Student can register to it."

    def check_course(self):
        """
        it will check  if particular course  registered in autgrader or not
        """
        course_code = self.payload['code']
        cursor = self.db_con.cursor()
        query = ("SELECT * FROM CODES_LIST"
         " WHERE CODE=%s")
        cursor.execute(query, (course_code, ))
        res = cursor.fetchone()
        self.log.debug("Result from CODE_LIST table {}".format(res))
        if res is None:
            return True
        else:
            return False
        return None
    
    def check_assing_task_exist(self):
        """
        check if task already exist to avoid duplication
        """
        type_ = self.payload['type']
        if type_ == "Task":
            logging.debug("Checking if task exist")
            number = self.payload['number']
            section = self.payload['section']
            #question = payload['questions']
            cursor = self.db_con.cursor()
            query = ("SELECT * FROM META_TASK"
            " WHERE TASK_NO=%s AND SECTION=%s")
            cursor.execute(query, (number,section))
            res = cursor.fetchone()
            self.log.debug("Result from CODE_LIST table {}".format(res))
            if res is None:
                return True
            else:
                return False
        elif type_ == "Assignment":
            self.log.debug("Checking Assignment in autograder")
            number = self.payload['number']
            #question = payload['questions']
            cursor = self.db_con.cursor()
            query = ("SELECT * FROM META_ASSIGN"
            " WHERE ASSIGN_NO=%s")
            cursor.execute(query, (number,))
            res = cursor.fetchone()
            self.log.debug("Result from Assignmeny table {}".format(res))
            if res is None:
                return True
            else:
                return False
    
    def check_assignmnet_deadline(self):
        """
        check two thing
        1. if task/assignment exist
        2. check the deadline
        3. check number of submission

        any condition false will return particular message stating above condition
        """
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        dt_time = datetime.strptime(dt_string, '%d-%m-%Y %H:%M:%S')
        # task number
        number = self.payload['number']
        coursecode =  self.payload['coursecode']

        if self.payload['type'] == "Task":
            self.log.debug("Checking for the task")
            section = self.payload['section']
            cursor = self.db_con.cursor()
            query = ("SELECT * FROM META_TASK"
                " WHERE TASK_NO=%s AND CODE=%s AND SECTION=%s")
            cursor.execute(query, (number,coursecode,section))
            res = cursor.fetchone()
            self.log.debug("Task meta data is:{}".format(res))

            ####### CHECKINFG IF STUDENTS IS REGISTERED IN THAT PARTICUALR COURSE
            # checking if task is present or not
            if res is None:
                return "Task not present, kindly check with instructor"
            # deadline checking
            deadline = res[3]
            if dt_time > deadline:
                return "Deadline Passed!Be on time next time :-"
            
            # checking student is belong to same section
            # task tection
            section_ = res[2]
            if section_ != section:
                return "Task for this section does not exist"
            return True
        
        if self.payload['type'] == "Assignment":
            self.log.debug("Checking for the ASSIGNMENT")
            cursor = self.db_con.cursor()
            query = ("SELECT * FROM META_ASSIGN"
                " WHERE ASSIGN_NO=%s AND CODE=%s")
            cursor.execute(query, (number,coursecode))
            res = cursor.fetchone()
            self.log.debug("ASSIGMENT meta data is:{}".format(res))
            # checking if task is present or not
            if res is None:
                return "Assignment not present, kindly check with instructor"
            # deadline checking
            deadline = res[2]
            self.log.debug("Deadline date for Assignment is:{}".format(deadline))
            if dt_time > deadline:
                return "Deadline Passed!Be on time next time :-"
            
            return True
        

    def return_deadline(self):
        """
        check two thing
        1. if task/assignment exist
        2. check the deadline
        3. check number of submission

        any condition false will return particular message stating above condition
        """
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        dt_time = datetime.strptime(dt_string, '%d-%m-%Y %H:%M:%S')
        # task number
        number = self.payload['number']
        coursecode =  self.payload['coursecode']

        if self.payload['type'] == "Task":
            self.log.debug("Checking for the task")
            section = self.payload['section']
            cursor = self.db_con.cursor()
            query = ("SELECT * FROM META_TASK"
                " WHERE TASK_NO=%s AND CODE=%s AND SECTION=%s")
            cursor.execute(query, (number,coursecode,section))
            res = cursor.fetchone()
            self.log.debug("Task meta data is:{}".format(res))
            # checking if task is present or not
            if res is None:
                return "Task not present, kindly check with instructor"
            # deadline checking
            deadline = res[3]
            if dt_time > deadline:
                return "Deadline Passed!Be on time next time :-"
            
            # checking student is belong to same section
            # task tection
            section_ = res[2]
            if section_ != section:
                return "Task for this section does not exist"
            return deadline
        
        if self.payload['type'] == "Assignment":
            self.log.debug("Checking for the ASSIGNMENT")
            cursor = self.db_con.cursor()
            query = ("SELECT * FROM META_ASSIGN"
                " WHERE ASSIGN_NO=%s AND CODE=%s")
            cursor.execute(query, (number,coursecode))
            res = cursor.fetchone()
            self.log.debug("ASSIGMENT meta data is:{}".format(res))
            # checking if task is present or not
            if res is None:
                return "Task not present, kindly check with instructor"
            # deadline checking
            deadline = res[2]
            self.log.debug("Deadline date for Assignment is:{}".format(deadline))
            if dt_time > deadline:
                return "Deadline Passed!Be on time next time :-"
            
            return True

    def check_student_course(self):
        """
        check if student course exist
        """

        cursor = self.db_con.cursor()
        query = ("SELECT * FROM META_ASSIGN"
        " WHERE ASSIGN_NO=%s AND TOTAL_QUESTION=%s")
        cursor.execute(query, (number,question))
        res = cursor.fetchone()
        self.log.debug("Result from CODE_LIST table {}".format(res))
        if res is None:
            return True
        else:
            return False

    def check_no_submission(self):
        """
        check if submission count increase
        """
        type_ = payload['type']
        if type_ == "TASK":
            number = payload['number']
            section = payload['section']
            cursor = self.db_con.cursor()
            query = ("SELECT * FROM META_TASK"
            " WHERE TASK_NO=%s AND SECTION=%s")
            cursor.execute(query, (number,section))
            res = cursor.fetchone()
            self.log.debug("Result from CODE_LIST table {}".format(res))
            if res is None:
                return True
            else:
                return False
        elif type_ == "ASSIGNMENT":
            number = payload['number']
            cursor = self.db_con.cursor()
            query = ("SELECT * FROM META_ASSIGN"
            " WHERE ASSIGN_NO=%s")
            cursor.execute(query, (number))
            res = cursor.fetchone()
            self.log.debug("Result from CODE_LIST table {}".format(res))
            if res is None:
                return True
            else:
                return False


    def add_student_to_course(self):
        """
        adding student to particular course
        """
        
        if self.check_student_registeration() == False:
            self.log.debug("check is pass")
            return "Student already register"

        if self.check_user_exist() == True:
            self.log.debug("check is pass")
            return "STUDENT IS NOT REGISTER IN AUTOGRADER, PLEASE REGISTER STUDENT FIRST"
        
        add_course = ("INSERT INTO STUDENTS_LIST "
               "(CODE,EMAIL,SECTION) "
               "VALUES (%s, %s, %s)")
        self.log.debug("name:{},code:{}".format(self.payload['email'], self.payload['coursecode']))
        course_data = (self.payload['coursecode'], self.payload['email'], self.payload['section'])
        cursor = self.db_con.cursor()
        cursor.execute(add_course, course_data)
        self.db_con.commit()
        '''
        Hi x.y.z,
        You have successfully registered in a new course. Details are stated below
        CourseCode: cl-201
        Email: p156058@nu.edu.pk
        Section: A
        '''
        #send_mail("faisal.khan@nu.edu.pk",self.email,"Your secured token for login is "+str(token))
        message = "Hi,\n You have successfully registered in a new course.Details are stated below\n\n    CourseCode: {0}\n    Email: {1}\n    Section: {2}\n\n\nRegards,\nFaisal khan"\
            .format(self.payload['coursecode'],self.payload['email'], self.payload['section'])
        send_mail("faisal.khan@nu.edu.pk", self.payload['email'] ,message, "Markar Course Registration Alert")
        return "STUDENT IS REGISTER SUCCESSFULLY"


    def validate_user(self):
        """
        validate wheather particular person is admin or not
        """
        cursor = self.db_con.cursor()
        query = ("SELECT * FROM STUDENTS "
                "WHERE token ==%s")
        cursor.execute(query,(self.token))

        return "nothing"

    def check_if_task_exist(self):
        """
        check if task already exist
        """

    def update_score(self):
        """
        update score in appropriate table
        """
        type_ = self.payload['type']
        if type_ == "Task":
            logging.debug("Adding the new task")
            number = self.payload['number']
            marks = self.payload['marks']
            #EMAIL = self.payload['EMAIL']
            email = self.payload['email']
            code = self.payload['coursecode']
            #question = payload['questions']
            cursor = self.db_con.cursor()
            add_students = ("SELECT OBTAINED_MARKS FROM TASKS"
            " WHERE TASK_NO=%s AND EMAIL=%s AND LAB_CODE=%s")
            #self.log.debug("rollNo:{},email:{},token:{}".format(self.EMAIL, self.email, str(token)))
            student_data = (number, email, code)
            cursor = self.db_con.cursor()
            cursor.execute(add_students, student_data)
            res = cursor.fetchone()
            if res is None:
                query = ("INSERT INTO TASKS()"
                        " VALUES(%s,%s,%s,%s,%s)")
                cursor = self.db_con.cursor()
                cursor.execute(query,(number, email, marks,code,1))
                self.db_con.commit()
            else:
                query = ("UPDATE TASKS SET OBTAINED_MARKS=%s "
                         "WHERE TASK_NO=%s AND EMAIL=%s AND LAB_CODE=%s")
                cursor = self.db_con.cursor()
                cursor.execute(query,(marks,number, email,code))
                self.db_con.commit()
                
                query = ("UPDATE TASKS SET SUBMISSION_STATUS=SUBMISSION_STATUS+1"
                        "WHERE TASK_NO=%s AND EMAIL=%s AND LAB_CODE=%s")
                cursor = self.db_con.cursor()
                cursor.execute(query,(marks,number, email,code))
                self.db_con.commit()

        elif type_ == "Assignment":
            logging.debug("Adding the new task")
            number = self.payload['number']
            marks = self.payload['marks']
            #EMAIL = self.payload['EMAIL']
            email = self.payload['email']
            code = self.payload['coursecode']
            #question = payload['questions']
            cursor = self.db_con.cursor()
            add_students = ("SELECT OBTAINED_MARKS FROM ASSIGNMENTS"
            " WHERE ASSIGNMENT_NO=%s AND EMAIL=%s AND CODE=%s")
            #self.log.debug("rollNo:{},email:{},token:{}".format(self.EMAIL, self.email, str(token)))
            student_data = (number, email, code)
            cursor = self.db_con.cursor()
            cursor.execute(add_students, student_data)
            res = cursor.fetchone()
            if res is None:
                query = ("INSERT INTO ASSIGNMENTS()"
                        " VALUES(%s,%s,%s,%s,%s)")
                cursor = self.db_con.cursor()
                cursor.execute(query,(number, email, marks,code,1))
                self.db_con.commit()
                
                query = ("UPDATE ASSIGNMENTS SET SUBMISSION_STATUS=SUBMISSION_STATUS+1"
                        " WHERE ASSIGNMENT_NO=%s AND EMAIL=%s AND CODE=%s")
                #self.log.debug("rollNo:{},email:{},token:{}".format(self.EMAIL, self.email, str(token)))
                student_data = (number, email, code)
                cursor = self.db_con.cursor()
                cursor.execute(query, student_data)
                self.db_con.commit()
            else:
                query = ("UPDATE ASSIGNMENTS SET OBTAINED_MARKS=%s "
                         "WHERE ASSIGNMENT_NO=%s AND EMAIL=%s AND CODE=%s")
                cursor = self.db_con.cursor()
                cursor.execute(query,(marks,number, email,code))
                self.db_con.commit()

    def add_task_assignm(self):
        """
        Adding new task
        """
        type_ = self.payload['type']
        if type_ == "Task":
            logging.debug("Adding the new task")
            number = self.payload['number']
            section = self.payload['section']
            date = self.payload['deadline']
            marks = self.payload['marks']
            code = self.payload['coursecode']
            #question = payload['questions']
            cursor = self.db_con.cursor()
            add_students = ("INSERT INTO META_TASK "
               "(TASK_NO, CODE, SECTION, DEADLINE,MARKS) "
               "VALUES (%s, %s, %s,%s,%s)")
            #self.log.debug("rollNo:{},email:{},token:{}".format(self.EMAIL, self.email, str(token)))
            student_data = (number, code,section,date, marks)
            cursor = self.db_con.cursor()
            cursor.execute(add_students, student_data)
            self.db_con.commit()
        elif type_ == "Assignment":
            logging.debug("Adding the new task")
            number = self.payload['number']
            date = self.payload['deadline']
            marks = self.payload['marks']
            code = self.payload['coursecode']
            #question = payload['questions']
            cursor = self.db_con.cursor()
            add_students = ("INSERT INTO META_ASSIGN "
               "(ASSIGN_NO, CODE, DEADLINE,MARKS) "
               "VALUES (%s, %s, %s,%s)")
            #self.log.debug("rollNo:{},email:{},token:{}".format(self.EMAIL, self.email, str(token)))
            student_data = (number, code,date, marks)
            cursor = self.db_con.cursor()
            cursor.execute(add_students, student_data)
            self.db_con.commit()