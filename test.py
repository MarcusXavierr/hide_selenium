from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
class Google:
    def chrome():
        chrome_options = Options()


        chrome_options.add_extension('/home/marcus/selenium/hide_selenium/firefox_extension.zip')

        driver = Chrome(options=chrome_options)
        return driver
