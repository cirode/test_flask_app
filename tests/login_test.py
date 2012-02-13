from test_helper import *
import re

class LoginTest(TestCase):    
    def test_logged_out_going_to_the_home_screen_should_send_me_to_the_login_screen(self):
        response = self.app.get('/')
        should_redirect_to('/login', response)
    
    def test_posting_username_and_password_should_redirect_to_home_page(self):
        username = "chris"
        password = "toasty"
        response = self.app.post('/login', data=dict(
                username=username,
                password=password
            ))
        should_redirect_to('/', response)
        
    def test_posting_username_and_password_should_log_you_in_and_keep_you_logged_in(self):
        username = "chris"
        password = "toasty"
        response = login_user(self, username, password)
        soup = BeautifulSoup(response.data)
        assert soup.find('a', id="logout")
        assert soup.find('.metanav', text=re.compile('Welcome {username}'.format(username=username)))
        #and after a refresh
        response = self.app.get('/')
        soup = BeautifulSoup(response.data)
        assert soup.find('a', id="logout")
        assert soup.find('.metanav', text=re.compile('Welcome {username}'.format(username=username)))
        
    def test_a_logged_in_user_should_be_able_to_log_out(self):
        username = "chris"
        password = "toasty"
        login_user(self, username, password)
        response = logout_user(self)
        soup = BeautifulSoup(response.data)
        assert not soup.find('a', id="logout")
        #and after a refresh
        response = self.app.get('/')
        soup = BeautifulSoup(response.data)
        assert not soup.find('a', id="logout")
        
        

if __name__ == '__main__':
    unittest.main()