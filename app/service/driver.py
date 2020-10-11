from app.service.db_service import DatabaseService

class Main:
    def __init__(self, service=None,email=None, roll_no=None,request_data = None, log=None,operation=None,token=None,user_type=None):
       # self.email = email
        self.roll_no = roll_no
        self.token = token
        self.log = log
        self.email = email
        self.output = None
        self.auth = False
        self.service_type = service
        self.operation = operation
        self.payload = request_data
        self.log.debug("Driver:{}{}".format(self.roll_no,self.email))
        if self.service_type == "db":
            self.service = DatabaseService(request_data=self.payload,email=self.email,roll_no=self.roll_no,logging=self.log, operation=self.operation, token=token, user_type=user_type)
        elif self.service_type == "grade":
            return "some grading"

    def update_data(self, request_data=None,service=None,email=None, roll_no=None, log=None,operation=None,token=None,user_type=None):
        """
        updating class data
        """
        self.roll_no = roll_no
        self.email = email
        self.opperation = operation
        self.service.operation = operation
        self.service.database.roll_no = roll_no
        self.service.database.email = email
        self.service.database.payload = request_data
        self.log.debug("Updates:{}{}".format(self.service.roll_no,self.service.email))

    def driver_function(self):
        #if operation == "register_user":
        self.service.run(self)
            
   