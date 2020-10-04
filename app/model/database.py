
from app.util.util import *
from app.configuration.config import *
import mysql.connector
class DB:
    def __init__(self, roll_no,logging,student_name=None, token=None):
        self.roll_no = roll_no
        self.token = token
        self.db_con = None
        self.log = logging
        self.student_name = student_name

    def create_connection(self):
        """
        it will create database base on configuration value
        """
        self.log.debug("creating connection")
        try:
            self.db_con = mysql.connector.connect(user=USER,password=PASS,host=MysqlAddress,
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
            self.log.debug("Created successfully")
            return "successfully establish connection"
        

    
    
    def validate_admin(self):
        """
        validate wheather particular person is admin or not
        """
        cursor = self.db_con.cursor()
        query = ("SELECT * FROM administrator "
         "WHERE token ==%s")
        cursor.execute(query, (self.token))
        res = cursor.fetchone()
            if res == 0:
                return False
            else:
                return True

    def registered_user(self):
        """
        Adding new user to db
        """
        token = generate_token()
        email = convert_into_email(self.roll_no)
        add_students = ("INSERT INTO STUDENTS "
               "(STUDENT_NAME, ROLL_NO, EMAIL, TOKEN) "
               "VALUES (%s, %s, %s, %s)")
        student_data = (self.student_name, self.roll_no, email, token)
        cursor.execute(add_students, student_data)
        self.db_con.commit()

    def validate_user(self, student_token):
        """
        validate wheather particular person is admin or not
        """
        cursor = self.db_con.cursor()
        query = ("SELECT * FROM STUDENTS "
         "WHERE token ==%s"
        cursor.execute(query,())

        return "nothing"
    
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