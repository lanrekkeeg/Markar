import sys
import os
from app.model.database import DB

class DatabaseService:

    def __init__(self, email=None,request_data=None, roll_no=None,logging=None, operation=None, token=None,user_type=None):
       # self.email = email
        self.roll_no = roll_no
        self.email = email
        self.token = token
        self.log = logging
        self.user_type = user_type
        self.operation = operation
        self.payload = request_data
        self.log.debug("{}{}".format(self.roll_no,self.email))
        self.database = DB(logging=self.log,request_data=self.payload, token=self.token,user_type=self.user_type,email=self.email)
    
    def run(self, driver):
        if self.operation == "register":
            self.log.debug("Calling register function")
            self.log.debug("Service:{}{}".format(self.roll_no,self.email))
            driver.output = self.database.register_user()

        if self.operation == "add_admin":
            driver.output = self.database.add_admin()

        if self.operation == "validate":
            #if self.user_type == "ADMIN":
                driver.auth = self.database.validate_admin()
            #if self.user_type == "STUDENTS":
        if self.operation == "course_code":
            driver.output = self.database.add_course_code()

        if self.operation == "add_student_to_course":
            driver.output = self.database.add_student_to_course()
        
        if self.operation == "check_student_in_course":
            driver.output = self.database.check_student_registeration()
        
        if self.operation == "check_assignmnet_deadline":
            driver.output = self.database.check_assignmnet_deadline()
        
        if self.operation == "add_task_assign":
            driver.output = self.database.add_task_assignm()
        
        if self.operation == "check_course":
            driver.output = self.database.check_course_code_exist()
        
        if self.operation == "check_task_assignment":
            driver.output = self.database.check_assing_task_exist()
        
        if self.operation == "update_score":
            driver.output = self.database.update_score()
        
        if self.operation == "return_deadline":
            driver.output = self.database.return_deadline()



        



