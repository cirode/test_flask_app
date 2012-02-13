#import sys
#sys.path.append('..') #load the parent package for manual test runs
import unittest, re
from os import fork, kill, waitpid, environ
environ['FLASK_ENVIRONMENT']='testing'
import application
from factories import *
from werkzeug.serving import run_simple
import signal
from selenium import webdriver
from BeautifulSoup import BeautifulSoup

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = application.app.test_client()
        
class SeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.app = application.app
        self.browser = webdriver.Firefox()
        self.url = 'http://{host}:{port}'.format(host=self.app.config["HOST"],port=self.app.config["PORT"])
        newpid = fork()
        if newpid == 0:
            self.run_test_server()
        else:
            self.test_server_pid = newpid
    
    def tearDown(self):
        kill(self.test_server_pid,signal.SIGTERM)
        waitpid(self.test_server_pid, 0)
        self.browser.close()
        
    def run_test_server(self):
        run_simple(self.app.config['HOST'],self.app.config['PORT'],self.app) #Need Test Environment Config
        
def should_redirect_to(url,response):
    assert response.status_code == 302
    assert re.search(url, response.headers['Location'])
    
def login_user(self, username, password):
    return self.app.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout_user(self):
    return self.app.get('/logout', follow_redirects=True)

if __name__ == '__main__':
    unittest.main()