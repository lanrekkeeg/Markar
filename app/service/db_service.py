import sys
import os
from app.model.database import DB

class DatabaseService:

    def __init__(self, email, roll_no, token=None):
       # self.email = email
        self.roll_no = roll_no
        self.token = token
        self.database = DB(roll_no,token)
    
    def driver_function(self, operation):
        if operation == "register_user":
            self.token = self.database.registered_user()
            
    def register_user(self):


