from uuid import uuid4
import re
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.configuration.config import *
import os
import logging
import yaml
import os
import xml.etree.ElementTree as ET
from copy import copy
logging.basicConfig(level=logging.DEBUG)
ALLOWED_EXTENSIONS = ['cpp']

def generate_token():
    """
    this function will generate token for user
    """
    rand_token = uuid4()
    return rand_token

def convert_into_email(roll_no):
    """
    this will convert p15-6058 into p156058@nu.edu.pk

    TODO: validation of roll no required
    """
    roll_clean = re.sub(r"-", "", roll_no)
    email = roll_clean+"@nu.edu.pk"
    return email

def format_rollNo(roll_no):
    """
    This fucntion will format the email
    """
    roll_clean = re.sub(r"-", "", roll_no)
    roll_clean = re.sub(r"P", "", roll_clean)
    roll_clean = 'p'+roll_clean
    logging.debug("Formatted roll no is:{}".format(roll_clean))
    return roll_clean




def read_password():
    """
    reading password from file
    """
    with open(passwordfile,'r') as handle:
        read = handle.read()
        return read

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_mail(sender, receiver, body, subject):
    """
    sending message to student
    """
    password = read_password()
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        print("Email sent")
    
def creat_default_course_folder(data):
    """
    This fucntion will create default table for course code.Default folder will be following 
     1. Assignment
     2. Course

    """
    coursecode = data['coursecode']
    task_path = storage+coursecode+"/Task"
    assign_path = storage+coursecode+"/Assignment"
    logging.debug("Creaating Defual folder for {}".format(coursecode))
    try:
        os.makedirs(task_path)
        os.makedirs(assign_path)
    except Exception as exp:
        logging.error("Unable to create folder failed with {}".format(str(exp)))

def validate_create_folder(data):
    """
    This function will create task folder / course folder / section folder / submission
    """
         # check if course folder exist
    type_ = data["type"]
    number = data["number"]
    #total_que = data['questions']
    course_code = data["coursecode"]
    try:
        section = data["section"]
    except Exception as ex:
        section = None
    #question = data['questions']
    base_path = storage+course_code+"/"+type_
    logging.debug(base_path)
    if (os.path.exists(base_path)):
        # Creaating task folder
        logging.debug("Dir exists")
        task_path = base_path + "/" + type_ + "-" + str(number)
        try:
            os.mkdir(task_path)
        except Exception as exp:
            logging.debug("Got Exception:{}".format(str(exp)))
        #for num_ in range(total_que):
        if type_ == "Task":
            question_path = task_path + "/" + section + "/submission"
        else:
            question_path = task_path + "/submission"
        try:
            os.makedirs(question_path)
        except Exception as exp:
            logging.debug("Got Exception:{}".format(str(exp)))
        if type_ == "Task":
            test_cases = task_path + "/" + section + "/test"
        else:
            test_cases = task_path + "/test"

        try:
            os.makedirs(test_cases)
            return test_cases
        except Exception as exp:
            logging.debug("Got Exception:{}".format(str(exp)))

def dictify(r,root=True):
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text:
        d["_text"]=r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

    # old logic needs to be use in future
def validate_create_folder_old_non_used(data):
    """
    This function will create task folder / course folder / section folder / submission
    """
         # check if course folder exist
    type_ = data["type"]
    number = data["number"]
    total_que = data['questions']
    course_code = data["coursecode"]
    try:
        section = data["section"]
    except Exception as ex:
        section = None
    question = data['questions']
    base_path = storage+course_code+"/"+type_
    logging.debug(base_path)
    if (os.path.exists(base_path)):
        # Creaating task folder
        logging.debug("Dir exists")
        task_path = base_path + "/" + type_ + "-" + str(number)
        try:
            os.mkdir(task_path)
        except Exception as exp:
            logging.debug("Got Exception:{}".format(str(exp)))
        for num_ in range(total_que):
            question_path = task_path + "/" + section + "/Q-"+ str(num_+1) + "/submission"
            try:
                os.makedirs(question_path)
            except Exception as exp:
                logging.debug("Got Exception:{}".format(str(exp)))
            test_cases = task_path + "/" + section + "/Q-"+ str(num_+1) + "/test"
            try:
                os.makedirs(test_cases)
            except Exception as exp:
                logging.debug("Got Exception:{}".format(str(exp)))


        