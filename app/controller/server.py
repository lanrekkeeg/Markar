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

@api.route('/grade',methods=['POST'])
def post():
    """Register user in database"""
    driver = Main("grade","p156058", "p156058",logging)
    driver.driver_function("test")
    return flask.jsonify({"output":driver.output})


        