from test_helper import *

class RootPageTest(SeleniumTestCase):
    
    def test_index_page_shows_title(self):
        self.browser.get(self.url+'/')
        assert "Collected" in self.browser.title
        
if __name__ == '__main__':
    unittest.main()