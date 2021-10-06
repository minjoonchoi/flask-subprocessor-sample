#!/usr/bin/env python
import sys

import logging

from util import eprint
from util import init_logging

init_logging(app_name='test')

logger = logging.getLogger(__name__)

def main():
    logger.info('1')
    logger.info('2')
    logger.info('3')
    try:
        raise RuntimeError()
    except Exception as e:
        logger.error('sub process error')
        sys.exit(1)
    

if __name__ == '__main__' :
    main()