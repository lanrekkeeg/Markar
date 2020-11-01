from app.service.db_service import DatabaseService
from app.service.driver import *
from app.util.util import *
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
        email =  self.payload['email']
        number = self.payload['number']
        coursecode = self.payload['coursecode']
        #trim_email = re.sub('[^A-Za-z0-9]+', '', email) 
        trim_email = email.split("@")
        trim_email = trim_email[0]
        # e.g. course-name/Task/Task-1/A/submissions

        Basepath = str()
        student_dir = str()
        if self.payload['type'] == 'Task':
            section = self.payload['section']
            Basepath = storage + coursecode + "/Task/Task-" + str(number) + '/' + section.capitalize()
        #file_name = trim_email + '_' + section + '_' + str(task_no)
            student_dir = Basepath + '/submission/' + trim_email
        elif self.payload['type'] == 'Assignment':
            Basepath = storage + coursecode + "/Assignment/Assignment-" + str(number)
        #file_name = trim_email + '_' + section + '_' + str(task_no)
            student_dir = Basepath + '/submission/' + trim_email
        self.log.debug("BasePath: {} \n studentDir: {}".format(Basepath, student_dir))
        # student folder will be created in submission folder
        if not os.path.isdir(student_dir):
            os.mkdir(student_dir)
            self.log.debug("creating folder for submission")
        
        #student_file_dir = student_dir
        student_code = self.request.files['Task-File']
        filename = student_code.filename
        student_file_dir = student_dir + "/" + filename
        student_report = student_dir + '/' + 'report.xml'
        #if not os.path.isfile(student_file_dir):
            # frist save the file
            #student_code = self.request.files['Task-File']
        student_code.save(student_file_dir)
        #if not os.path.isfile(student_report):

        self.start_checking(Basepath,student_file_dir, student_report)
        report_output = self.generate_report(student_report)
        return report_output
        
    def start_checking(self, Basepath, student_file_dir, report):
        """
        checking the task
        """

        # load the test case file
        File = Basepath + '/test'
        # expecting only one file
        test_files = os.listdir(File)
        self.log.debug("test_file_name: {}".format(test_files[0]))
        test_files = test_files[0]
        File += '/' + test_files
        import subprocess
        #import os
        #file = open(File, 'r').read().strip()
        #file = file.replace("<<DIR>>", student_file_dir)
        #file = file.replace("<<REPORT>>", report)

        #write_file = open(File, 'w')
        #write_file.write(file)
        #write_file.close()
        #self.log.debug("Code: {}".format(file))
        from subprocess import Popen
        try:
            logging.debug("Test: {}\nstudentFile:{}\nreportDir:{}\n".format(File,student_file_dir,report))
            command = "python {0} \"{1}\" \"{2}\""\
                .format(File, student_file_dir, report)
            self.log.debug("Command: {}".format(command))
            #out = Popen(command)#("python "+File+ " "+student_file_dir+" "+report)
            out = subprocess.call(['python', File, report, student_file_dir])
            self.log.debug("command output: {}".format(out))
            #self.log.debug("{}".format(subprocess.run(["python", file])))
        except Exception as exp:
            self.log.error("Failed to load the file,Got following error {}".format(exp))
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
        root = ET.fromstring(file_)
        report_dict = dictify(root)
        REPORT = str()
        test_cases = report_dict['testsuites']['testsuite'][0]
        i = 1
        score = 0
        for ds in test_cases['testcase']:
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