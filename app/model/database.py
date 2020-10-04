
from app.util.util import *
from app.configuration.config import *
import mysql.connector
class DB:
    def __init__(self, roll_no,logging, token=None):
        self.roll_no = roll_no
        self.token = token
        self.db_con = None
        self.log = logging

    def create_connection(self):
        """
        it will create database base on configuration value
        """
        try:
            cnx = mysql.connector.connect(user=USER,password=PASS,host=MysqlAddress,
                                        database=DBName)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        return "successfully establish connection"
        

    def registered_user(self):
        return "nothing"
    
    def validate_user(self):
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