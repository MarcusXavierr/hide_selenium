from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import requests
class Google:
    def download_url(self, url, save_path, chunk_size=128):
        r = requests.get(self.url, stream=True)
        with open(self.save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=self.chunk_size):
                fd.write(chunk)
    def chrome(self):
        chrome_options = Options()
        
        try:
            chrome_options.add_extension('firefox.zip')
        except:
            self.download_url('https://github.com/MarcusXavierr/hide_selenium/raw/main/firefox_extension.zip','./firefox.zip')
            chrome_options.add_extension('firefox.zip')
            
        driver = Chrome(options=chrome_options)
        return driver
