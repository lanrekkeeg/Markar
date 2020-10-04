import sys
import os
from app.model.database import DB

class DatabaseService:

    def __init__(self, email, roll_no,logging, token=None):
       # self.email = email
        self.roll_no = roll_no
        self.token = token
        self.database = DB(roll_no,token)
        self.log = logging
    
    def driver_function(self, driver, operation):
        if operation == "register_user":
            driver.token = self.database.registered_user()
        if operation == "testConnection":
            self.database.create_connection()


    def register_user(self):
        return "None"


