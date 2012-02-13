from test_helper import *
import re

class CacheBustingTest(TestCase):
    
    def test_css_files_have_cache_busting_implemented(self):
        response = self.app.get('/')
        soup = BeautifulSoup(response.data)
        for style_tag in soup.findAll('link'):
            assert re.match('.*?cache_busting=.*', style_tag['href'])
            
    def test_javasccript_files_have_cache_busting_implemented(self):
        response = self.app.get('/')
        soup = BeautifulSoup(response.data)
        for js_tag in soup.findAll('script', {type: 'text/javascript'}):
            assert re.match('.*?cache_busting=.*', js_tag['src'])
        
if __name__ == '__main__':
    unittest.main()