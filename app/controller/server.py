from flask import request, make_response, Flask
import flask
from app.configuration.config import *
from app.service.driver import * 
from app.util.util import  *
import logging
import yaml
import os
import json

logging.basicConfig(level=logging.DEBUG)

# need to import the base level configuration
UPLOAD_FOLDER = storage
api = Flask(__name__)
api.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@api.route('/test',methods=['POST'])
def test():
    """Register user in database"""

    try:
        json_of_metadatas = request.form.to_dict(flat=False)
        data = json_of_metadatas['data'][0]
        data = json.loads(data)
        #logging.debug(json.loads(data))
        
    except Exception as exp:
        logging.error("Got error in feteching json data {}".format(str(exp)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("check for authorization")
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Admin = Main(service="db", log=logging, email=data['email'], token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
        driver_Admin.driver_function()
        if driver_Admin.auth:
            logging.debug("Autthorized Admin")
            driver_Admin = Main(service="db", log=logging, request_data=data, user_type="ADMIN", operation="check_course")
            driver_Admin.driver_function()
            if not driver_Admin.output:
                logging.debug("Course Exist")
                driver_Admin = Main(service="db", log=logging, request_data=data, user_type="ADMIN", operation="check_task_assignment")
                driver_Admin.driver_function()
                if driver_Admin.output:
                    logging.debug("Creating task/Assign as it does not exist")
                    test_case_path = validate_create_folder(data)
                    test_cases = request.files['upload_file']
                    test_cases.save(test_case_path+'/'+test_cases.filename)
                    driver_Admin.update_data(request_data= data,operation="add_task_assign")
                    driver_Admin.driver_function()
    
    # if you want to save it
    #picture.save('path/to/save')

    return 'ok', 200
   # return flask.jsonify({"output":driver.output})

@api.route('/AddCourse',methods=['POST'])
def add_course_code():
    """AddingCourse in the autograder database"""
    try:
        data = request.get_json()
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Admin = Main(service="db", log=logging, email=data['admin_email'], token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
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
        driver_Admin = Main(service="db", log=logging,email=data['admin_email'], token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
        driver_Admin.driver_function()
        if driver_Admin.auth:
            logging.debug("Autthorized Admin")
            # first needs to check if student is registered or not
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
        #driver_Admin = None
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Admin = Main(service="db", log=logging, email=data['admin_email'],token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
        driver_Admin.driver_function()
        if driver_Admin.auth:
            logging.debug("Autthorized Admin")
            # CHECKING IF STUDENT IS REGISTERED IN AUTOGRADER
            name = data['name']
            email = data['email']
            logging.debug("Serverr:{}{}".format(name,email))
            logging.debug("Adding new user")
            driver_Admin.update_data(request_data=data, name=name, email=email, operation="register")
            driver_Admin.driver_function()
        else:
            return flask.jsonify({"output": "UnAuthorized admin"})
    #return flask.jsonify({"output":request.headers.get('authorization')})

    #driver = Main("db","p156058", "p156058",logging,"test")
    #driver.driver_function()
    return flask.jsonify({"output":driver_Admin.output})


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
    out = str()
    try:
        json_of_metadatas = request.form.to_dict(flat=False)
        data = json_of_metadatas['data'][0]
        data = json.loads(data)
    except Exception as e:
        logging.error("error in decoding data coming through request, the error message is {}".format(str(e)))
    if request.headers.get("authorization") is not None:
        # validating admin
        logging.debug("Token is {}".format(request.headers.get("authorization")))
        driver_Student = Main(service="db", log=logging, roll_no = data['roll_no'], token=request.headers.get("authorization"), user_type="STUDENTS", operation="validate")
        driver_Student.driver_function()
        if driver_Student.auth:
            # now checking student in course
            driver_Student.update_data(request_data=data, operation="check_student_in_course")
            driver_Student.driver_function()
            out = driver_Student.output

            if not driver_Student.output:
               # return flask.jsonify({"output":"Student register into course"})
                # checking if assingment and deadline exist
                driver_Student.update_data(request_data=data, operation="check_assignmnet_deadline")
                driver_Student.driver_function()
                out = driver_Student.output
                # all condition met now checking for the assignment 
                if driver_Student.output == True:
                    driver_Student = Main(service="grade",request=request, log=logging,request_data=data, operation="submit")
                    driver_Student.driver_function()
                    out = driver_Student.output


        else:
            return flask.jsonify({"output": "UnAuthorized admin"})
    return flask.jsonify({"output":request.headers.get('authorization')})

    #driver = Main("db","p156058", "p156058",logging,"test")
    #driver.driver_function()
    return flask.jsonify({"output":driver_Student.output})
    

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


        