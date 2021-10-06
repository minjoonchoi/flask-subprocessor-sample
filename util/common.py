from __future__ import print_function
import os
import sys

import logging
from logging.handlers import TimedRotatingFileHandler

def init_logging(app_name):
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    fileHandler = TimedRotatingFileHandler(os.path.join(log_dir, f'{app_name}.log'),
                                        when='D',
                                        interval=1,
                                        encoding='utf-8') 

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s > %(message)s',
        handlers=[
            fileHandler,
            logging.StreamHandler(stream=sys.stdout)
        ]
    )
