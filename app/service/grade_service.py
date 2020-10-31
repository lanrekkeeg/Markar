from app.service.db_service import DatabaseService
from app.service.driver import *
from app.configuration.config import *
import re
import os
import xml.etree.ElementTree as ET

class GradeService:
    def __init__(self, request=None, request_data=None, email=None,logging=None, operation=None, token=None,user_type=None):
       # self.email = email
        self.email = email
        self.token = token
        self.log = logging
        self.user_type = user_type
        self.payload = request_data
        self.request = request
        self.operation = operation
        self.log.debug("{}{}".format(self.email,self.email))

    def run(self, driver):
        if self.operation == "submit":
            driver.output = self.submit_task()

        
    def submit_task(self):
        """
        all the steps required to submit task

        1. token
        2. section incase of task
        3. roll no
        4. task no
        """
        section = self.payload['section']
        email =  self.payload['email']
        task_no = self.payload['number']
        coursecode = self.payload['coursecode']
        trim_email = re.sub('[^A-Za-z0-9]+', '', email) 
        # e.g. course-name/Task/Task-1/A/submissions
        Basepath = storage + coursecode + "/Task/Task-" + str(task_no) + '/' + section.capitalize()
        file_name = trim_email + '_' + section + '_' + str(task_no)
        student_dir = Basepath + '/submission/' + trim_email
        
        # student wolder will be created in submission folder
        if not os.path.isdir(student_dir):
            os.mkdir(student_dir)
        
        student_file_dir = student_dir + '/' + file_name
        student_report = student_dir + '/' + 'report.xml'
        if not os.path.isfile(student_file_dir):
            # frist save the file
            student_code = self.request.files['Task-File']
            student_code.save(student_file_dir)
        
        start_checking(Basepath,student_file_dir)
        report_output = generate_report(student_report)
        return report_output
        
        # check the number
        # calculate results
        # task path

        # test case path

    
    def start_checking(self, Basepath, student_file_dir):
        """
        checking the task
        """

        # load the test case file
        File = Basepath + '/test'
        # expecting only one file
        test_files = arr = os.listdir(File)
        test_files = test_files[0]
        File = '/' + test_files
        print(test_files[i])
        import subprocess
        file = open(File, 'r').read().strip()
        file = file.replace("<<DIR>>", student_file_dir)
        file = file.replace("<<REPORT>>", report_path)
        logging.debug("{}".format(subprocess.run(["python", File], capture_output=True)))
        #print(subprocess.run(["python", "unittest_.py"], capture_output=True))


    
    def update_score(self):
        """
        calculating number for particular assingment
        """
        driver = Main(service='db',operation='update_score',request_data=self.payload)
        driver.driver_function()


    def generate_report(self, report_path):
        """
        Generating the report
        """
        file_ = open(report_path,'r').read().strip()
        i = 1
        score = 0
        for ds in ls['testcase']:
            if ds.get("failure",None) is not None:
                REPORT += "Test-Case-{0}, outcome:{1}, AssertError:{2}\n"\
                    .format(str(i), "Fail", ds['failure'][0]['_text'])
                #REPORT.update({"TEST-"+str(i):ds['name'], "outcome":"Fail", "AssertError":ds['failure'][0]['_text']})
            else:
                REPORT += "Test-Case-{0}, outcome:{1}\n"\
                    .format(str(i), "Pass")
                score +=1
            i += 1
        self.payload['marks'] = score
        return REPORT