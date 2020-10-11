from uuid import uuid4
import re
import smtplib, ssl
from app.configuration.config import *

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