from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
class Google:
    def chrome():
        chrome_options = Options()
        
        
        chrome_options.add_extension('')

        driver = Chrome(options=chrome_options)
        return driver
