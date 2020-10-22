from uuid import uuid4
import re
import smtplib, ssl
from app.configuration.config import *
import os
import logging
import yaml
import os
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

def send_mail(sender, receiver, message):
    """
    sending message to student
    """
    password = read_password()
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Email sent")
    
def validate_create_folder(data):
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


        