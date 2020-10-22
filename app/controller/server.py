from flask import request, make_response, Flask
import flask
from app.configuration.config import *
from app.service.driver import * 
from app.util.util import  *
import logging
import yaml
import os
logging.basicConfig(level=logging.DEBUG)

# need to import the base level configuration
UPLOAD_FOLDER = storage
api = Flask(__name__)
api.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@api.route('/test',methods=['POST'])
def test():
    """Register user in database"""

    
    try:
        import json
        json_of_metadatas = request.form.to_dict(flat=False)
        data = json_of_metadatas['data'][0]
        data = json.loads(data)
        #logging.debug(json.loads(data))
        
    except Exception as exp:
        logging.error("Got error in feteching json data {}".format(str(exp)))
    # checking

    # create necassary folders
    validate_create_folder(data)

    #databse insertion

    ## check if 
    input1 = request.files['upload_file']
    print("Name ",input1.filename)
    print(input1)
    #input1.save(os.getcwd()+input1.filename)
    '''
    input1 = request.files['input1']
    output1 = request.files.get('output1')
    input2 = request.files.get('input2')
    output2 = request.files.get('output2')
    print("Name ",input1.filename)
    return "nothing"
    output1.save(os.getcwd()+input1.filename)
    '''
   
    # TODO
    # 1. Authenticate user
    # 2. check courese
    # 3. check if teacher is studying that course 
    # 4. check if folder exist
    #   . code
    #     . section
    #       . task-no
    #         . solution
    #         . submissions
    #           . roll_no/email
    #           . autograder_results/logs
    #  incase of student submission
    #   check for assignment/ task deadline
    #   check section
    #   check submission count
    #   create /code/section/task-no/Q-1/submission/roll-no
    #   create /code/section/task-no/Q-1/submission/autograder_result

    
    # if you want to save it
    #picture.save('path/to/save')

    return 'ok', 200
   # return flask.jsonify({"output":driver.output})

@api.route('/CourseCode',methods=['POST'])
def add_course_code():
    """Register user in database"""
    try:
        data = request.get_json()
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Admin = Main(service="db", log=logging, email=data['email'], token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
        driver_Admin.driver_function()
        if driver_Admin.auth:
            logging.debug("Autthorized Admin")
            driver_Admin.update_data(request_data= data,operation="course_code")
            driver_Admin.driver_function()
            return flask.jsonify({"output":driver_Admin.output})

        else:
            return flask.jsonify({"output": "UnAuthorized admin"})
    return flask.jsonify({"output":"TOKEN IS MISSING"})

    #driver = Main("db","p156058", "p156058",logging,"test")
    #driver.driver_function()
    return flask.jsonify({"output":driver.output})

@api.route('/AddStudentToCourse',methods=['POST'])
def add_student_to_course():
    """Adding student to course"""
    try:
        data = request.get_json()
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Admin = Main(service="db", log=logging,email=data['email'], token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
        driver_Admin.driver_function()
        if driver_Admin.auth:
            logging.debug("Autthorized Admin")
            driver_Admin.update_data(request_data= data,operation="add_student_to_course")
            driver_Admin.driver_function()
            return flask.jsonify({"output":driver_Admin.output})

        else:
            return flask.jsonify({"output": "UnAuthorized admin"})
    return flask.jsonify({"output":"TOKEN IS MISSING"})

    #driver = Main("db","p156058", "p156058",logging,"test")
    #driver.driver_function()
    return flask.jsonify({"output":driver.output})

@api.route('/AddTask',methods=['POST'])
def add_task():
    """Adding New Task"""
    try:
        data = request.get_json()
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Admin = Main(service="db", log=logging, email=data['email'],token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
        driver_Admin.driver_function()
        if driver_Admin.auth:
            logging.debug("Autthorized Admin")
            driver_Admin.update_data(request_data= data,operation="add_task")
            driver_Admin.driver_function()
            return flask.jsonify({"output":driver_Admin.output})

        else:
            return flask.jsonify({"output": "UnAuthorized admin"})
    return flask.jsonify({"output":"TOKEN IS MISSING"})

    #driver = Main("db","p156058", "p156058",logging,"test")
    #driver.driver_function()
    return flask.jsonify({"output":driver.output})

@api.route('/RegisterStudent',methods=['POST'])
def register_student():
    """Register user in database"""
    try:
        data = request.get_json()
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Admin = Main(service="db", log=logging, email=data['email'],token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
        driver_Admin.driver_function()
        if driver_Admin.auth:
            logging.debug("Autthorized Admin")
            roll_no = data['roll_no']
            email = data['email']
            logging.debug("Serverr:{}{}".format(roll_no,email))
            logging.debug("Adding new user")
            driver_Admin.update_data(roll_no=roll_no, email=email, operation="register")
            driver_Admin.driver_function()

        else:
            return flask.jsonify({"output": "UnAuthorized admin"})
    return flask.jsonify({"output":request.headers.get('authorization')})

    #driver = Main("db","p156058", "p156058",logging,"test")
    #driver.driver_function()
    return flask.jsonify({"output":driver.output})


@api.route('/AddAssignment',methods=['POST'])
def add_assignment():
    try:
        data = request.get_json()
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        roll_no = data['rollNo']
        name = data['name']
        driver = Main("db","p156058", "p156058",logging,"validate_admin",token=request.headers.get("authorization"))
        driver.driver_function()
    else:
        return flask.jsonify({"output": "UnAuthorized admin"})


@api.route('/SubmitTest',methods=['POST'])
def submit_test():
    """
    Test submission
    """
    try:
        data = request.get_json()
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Student = Main(service="db", log=logging,email=data['email'], token=request.headers.get("authorization"), user_type="STUDENTS", operation="validate")
        driver_Student.driver_function()
        if driver_Student.auth:
            logging.debug("Autthorized Student")
            return flask.jsonify({"output":"Authorized Student"})
            email = data['email']
            language = data['lang']
            type_ = data['type']

            ## first it will run the test
            ## second it will store the results
            driver_Student = Main(service="db", log=logging,email=data['email'], token=request.headers.get("authorization"), user_type="STUDENTS", operation="submit")
            driver_Student.driver_function()

        else:
            return flask.jsonify({"output": "UnAuthorized admin"})
    return flask.jsonify({"output":request.headers.get('authorization')})

    #driver = Main("db","p156058", "p156058",logging,"test")
    #driver.driver_function()
    return flask.jsonify({"output":driver.output})
    

@api.route('/SubmitFinal',methods=['POST'])
def submit_final():
    try:
        data = request.get_json()
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        roll_no = data['rollNo']
        name = data['name']
        driver = Main("db", roll_no=roll_no,logging=logging,operation="validate",token=request.headers.get("authorization"))
        driver.driver_function()
    else:
        return flask.jsonify({"output": "UnAuthorized admin"})


@api.route('/grade',methods=['POST'])
def post():
    """Register user in database"""
    driver = Main("grade","p156058", "p156058",logging)
    driver.driver_function("test")
    return flask.jsonify({"output":driver.output})


        