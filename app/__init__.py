  
# app/__init__.py

from flask_restx import Api
from flask import Blueprint, request
import logging

from .main.controller.transaction_controller import api as transaction_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='Acerta House Price Prediction API',
          version='1.0',
          description='Input house features and return house price'
          )

api.add_namespace(transaction_ns, path='/price')


@blueprint.app_errorhandler(404)
def error_404(error):
    logging.critical(error)
    
    response_obj={
        'HTML Error Type': str(error.code),
        'message':'The resource was not found!',
        'description': error.description
    }
    return response_obj, 404

@blueprint.app_errorhandler(401)
def error_401(error):
    logging.critical(error)
    
    response_obj={
        'HTML Type': str(error.code),
        'message':'The resource was not found!',
        'description': error.description
    }
    return response_obj, 401

@blueprint.app_errorhandler(409)
def error_409(error):
    logging.critical(error)
    
    response_obj={
        'message':'Service error occured'
    }
    return response_obj, 409

@blueprint.app_errorhandler(500)
def error_500(error):
    logging.critical(error)
    
    response_obj={
        'HTML Type': str(error.code),
        'message':'The resource was not found!',
        'description': error.description
    }
    return response_obj, 500