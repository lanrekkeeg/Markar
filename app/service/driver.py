from app.service.db_service import DatabaseService

class Main:
    def __init__(self, service_type,email, roll_no, logging,operation=None,token=None):
       # self.email = email
        self.roll_no = roll_no
        self.token = token
        self.log = logging
        self.email = email
        self.output = None
        if service_type == "db":
            self.service = DatabaseService(self.email,self.roll_no,self.log, operation, token)
        elif service_type == "grade":
            return "some grading"
    
    def driver_function(self):
        #if operation == "register_user":
        self.service.run(self)
            
   