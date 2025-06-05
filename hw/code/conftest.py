from ui.fixtures import *
from typing import Dict, Any
import dotenv
import os
from utils.session import read_session_from_file

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://ads.vk.com/')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
    }

@pytest.fixture(scope='session')
def session() -> Dict[str, Any]:
    session = read_session_from_file()
    if session is None:
        return {
            'cookie': None,
            'local_storage': None
        }
    return session

@pytest.fixture(scope='session')
def credentials():
        dotenv.load_dotenv()
        return {"phone_number": os.getenv("PHONE"), "password": os.getenv("PASSWORD")}
