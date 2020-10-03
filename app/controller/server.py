from flask import request, make_response
from flask_restplus import Resource, Namespace
from autograder.driver import 
import logging
import yaml
logging.basicConfig(level=logging.DEBUG)

# need to import the base level configuration


@api.route('/registration')
def post():
    """Register user in database"""
        