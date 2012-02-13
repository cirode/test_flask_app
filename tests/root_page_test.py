from test_helper import *

class RootPageTest(TestCase):
    
    def test_index_page_shows_title(self):
        rv = self.app.get('/')
        print rv
        
if __name__ == '__main__':
    unittest.main()