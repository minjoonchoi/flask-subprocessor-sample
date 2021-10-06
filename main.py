#!/usr/bin/env python
import os
import sys
import logging
    
from flask import Flask
from flask_restful import Api

from util import init_logging
from api import SubProcess

init_logging(app_name='flask')

logger = logging.getLogger(__name__)

app = Flask(__name__)

api = Api(app)
api.add_resource(SubProcess, '/execute')

def main():
    logger.info('Executing Flask app...')
    app.run(debug=True)

if __name__ == '__main__':
    main()