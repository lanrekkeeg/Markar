
from app.util.util import *
from app.configuration.config import *
import mysql.connector
from mysql.connector import errorcode

class DB:
    def __init__(self, roll_no=None,logging=None,email=None, token=None,request_data=None, user_type=None):
        self.log = logging
        self.roll_no = roll_no
        self.token = token
        self.payload  = request_data
        self.user_type = user_type
        self.db_con = self.create_connection()
        self.email = email


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
        #email = convert_into_email(self.roll_no)
        add_students = ("INSERT INTO STUDENTS "
               "(ROLL_NO, EMAIL, TOKEN) "
               "VALUES (%s, %s, %s)")
        self.log.debug("rollNo:{},email:{},token:{}".format(self.roll_no, self.email, str(token)))
        student_data = (self.roll_no, self.email, str(token))
        cursor = self.db_con.cursor()
        cursor.execute(add_students, student_data)
        self.db_con.commit()
    
        send_mail("faisal.khan@nu.edu.pk",self.email,"Your secured token for login is "+str(token))
        return "Student register"

    def check_user_exist(self):
        """
        checking if user already exist
        """
        cursor = self.db_con.cursor()
        query = ("SELECT * FROM STUDENTS"
         " WHERE ROLL_NO=%s")
        self.log.debug("Query:{}".format(query))
        cursor.execute(query, (self.roll_no,))
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
        code_name = self.payload['code']
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

    def check_student_registeration(self):
        """
        check if student is registetere to particular course
        """
        code_name = self.payload['code']
        roll_no = self.payload['roll_no']
        cursor = self.db_con.cursor()
        query = ("SELECT * FROM COURSES"
         " WHERE COURSE_CODE=%s AND ROLL_NO=%s")
        cursor.execute(query, (code_name,roll_no))
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
        self.log.debug("name:{},code:{}".format(self.payload['name'], self.payload['code']))
        course_data = (self.payload['name'], self.payload['code'])
        cursor = self.db_con.cursor()
        cursor.execute(add_course, course_data)
        self.db_con.commit()
    
        #send_mail("faisal.khan@nu.edu.pk",self.email,"Your secured token for login is "+str(token))
        return "Course Added, Student can register to it."

    def add_student_to_course(self):
        """
        adding student to particular course
        """
        
        if self.check_student_registeration() == False:
            self.log.debug("check is pass")
            return "Student already register"
        
        add_course = ("INSERT INTO COURSES "
               "(COURSE_CODE,ROLL_NO,C_SECTION) "
               "VALUES (%s, %s, %s)")
        self.log.debug("name:{},code:{}".format(self.payload['roll_no'], self.payload['code']))
        course_data = (self.payload['code'], self.payload['roll_no'], self.payload['section'])
        cursor = self.db_con.cursor()
        cursor.execute(add_course, course_data)
        self.db_con.commit()
    
        #send_mail("faisal.khan@nu.edu.pk",self.email,"Your secured token for login is "+str(token))
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
    def add_task():
        """
        Adding new task
        """

    
    def get_assignment_metadata(self):
        return "nothing"
    
    def submit_score(self):
        return "nothing"
    
    def add_submition_entry(self):
        return "nothing"
    
    def create_assignment_entry(self):
        return "nothing"
    def task_task_entry(self):
        return "nothing"