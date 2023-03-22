import os
import sys

import pytest
import datetime
import argparse
WORK_DIR = os.getcwd()
THIS_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
print('WORK_DIR', WORK_DIR)
print('THIS_FILE_DIR', THIS_FILE_DIR)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
# from ..data.enums.devices import Devices
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    current_execution_date = datetime.datetime.now().strftime("%I-%M-%S %p | %m:%d:%Y")
    name: str = "API Regression: " + current_execution_date
    pytest.main(['-q', '-s', '--testrail',
                 '--tr-testrun-name', name,
                 # '--device', args.device.value,
                 '--tr-config', 'config/testrail.cfg',
                 'functional/geo/get_cities_test.py'])

    # pytest.main(['-q', '-s',
    #              '--device', args.device.value,
    #              '../../mobile_automation/login_test.py'])