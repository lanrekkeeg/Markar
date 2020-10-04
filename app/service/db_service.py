import sys
import os
from app.model.database import DB

class DatabaseService:

    def __init__(self, email, roll_no,logging, operation, token=None):
       # self.email = email
        self.roll_no = roll_no
        self.token = token
        self.log = logging
        self.operation = operation
        self.database = DB(self.roll_no,self.log, self.token)
    
    def run(self, driver):
        if self.operation == "register_user":
            driver.output = self.database.registered_user()
        if self.operation == "test":
            driver.output = self.database.create_connection()




