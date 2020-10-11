from flask import request, make_response, Flask
import flask
from app.service.driver import * 
import logging
import yaml
logging.basicConfig(level=logging.DEBUG)

# need to import the base level configuration

api = Flask(__name__)

@api.route('/test',methods=['POST'])
def test():
    """Register user in database"""
    driver = Main("db","p156058", "p156058",logging,"test")
    driver.driver_function()
    return flask.jsonify({"output":driver.output})

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
        driver_Admin = Main(service="db", log=logging, token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
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
        driver_Admin = Main(service="db", log=logging, token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
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
        driver_Admin = Main(service="db", log=logging, token=request.headers.get("authorization"), user_type="ADMIN", operation="validate")
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

@api.route('/AddTask',methods=['POST'])
def add_task():
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
        driver = Main("db","p156058", "p156058",logging,"validate_admin",token=request.headers.get("authorization"))
        driver.driver_function()
    else:
        return flask.jsonify({"output": "UnAuthorized admin"})


@api.route('/grade',methods=['POST'])
def post():
    """Register user in database"""
    driver = Main("grade","p156058", "p156058",logging)
    driver.driver_function("test")
    return flask.jsonify({"output":driver.output})


        