import subprocess
from subprocess import SubprocessError, check_output
import logging
from flask_restful import reqparse, abort, Resource

logger = logging.getLogger(__name__)

parser = reqparse.RequestParser()
parser.add_argument('script', type=str)

class SubProcess(Resource):
    def post(self):
        args = parser.parse_args()
        logger.info(f'\n[HTTP ARGS] {args}')
        cmd = f'python {args.script}.py'
        try:
            out = check_output(cmd, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
            logger.info(f'\n[SUCCESS] {cmd}')
            logger.info(f'\n[OUTPUT] \n{out}')
            return {'command': cmd, 'status': 'success', 'message': out }
        
        except SubprocessError as err:
            logger.error(f'\n[FAIL] {cmd}')
            logger.error(f'\n[OUTPUT] \n{err.stdout}')
            return {'command': cmd, 'status': 'fail', 'message': str(err)}
    
    def get(self):
        return {'status': 'success'}