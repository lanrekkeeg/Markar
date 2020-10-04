from app.service.db_service import DatabaseService

class Main:
    def __init__(self, email, roll_no, logging,token=None):
       # self.email = email
        self.roll_no = roll_no
        self.token = token
        self.log = logging
        self.email = email
        self.database = DatabaseService(self.email,self.roll_no,self.log,token)
    
    def driver_function(self, operation):
        #if operation == "register_user":
        self.database.driver_function(self, operation)
            
            
    def register_user(self):
        return "none"