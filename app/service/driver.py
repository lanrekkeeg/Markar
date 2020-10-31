from app.service.db_service import DatabaseService
from app.service.grade_service import GradeService

class Main:
    def __init__(self, name=None,service=None,request=None,email=None, roll_no=None,request_data = None, log=None,operation=None,token=None,user_type=None):
       # self.email = email
        self.token = token
        self.log = log
        self.email = email
        self.output = None
        self.auth = False
        self.service_type = service
        self.operation = operation
        self.payload = request_data
        self.name = name
        if self.service_type == "db":
            self.service = DatabaseService(request_data=self.payload,email=self.email,logging=self.log, operation=self.operation, token=token, user_type=user_type)
        elif self.service_type == "grade":
            self.service = GradeService(request=request, request_data=self.payload,email=self.email,logging=self.log, operation=self.operation, token=token, user_type=user_type)

    def update_data(self,name=None,request_data=None,service=None,email=None, log=None,operation=None,token=None,user_type=None):
        """
        updating class data
        """
        self.name = name
        self.email = email
        self.opperation = operation
        self.service.name = name
        self.service.operation = operation
        self.service.database.email = email
        self.service.database.payload = request_data

    def driver_function(self):
        #if operation == "register_user":
        self.service.run(self)
            
   