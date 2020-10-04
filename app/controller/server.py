from flask import request, make_response, Flask
import flask
from app.service.driver import * 
import logging
import yaml
logging.basicConfig(level=logging.DEBUG)

# need to import the base level configuration

api = Flask(__name__)

@api.route('/test',methods=['POST'])
def post():
    """Register user in database"""
    driver = Main("p156058", "p156058",logging)
    out = driver.driver_function("test")
    return flask.jsonify({"output":out})
        