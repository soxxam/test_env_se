from selenium import webdriver
import pathlib
import teepublic.constants as const
from selenium.webdriver.common.by import By

path = pathlib.Path().resolve()

class Teepublic(webdriver.Chrome):
    def __init__(self, driver_path= str(path) + '\chromedriver.exe',teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Teepublic, self).__init__(executable_path = self.driver_path, options=options)
        self.implicitly_wait(30)
        self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)