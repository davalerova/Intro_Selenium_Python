import unittest
import time
from selenium.webdriver.support.ui import Select

from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class AutomaticNavigation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\daval\Desktop\Platzi\Curso de introduccion a Selenium con Python\Scripts\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://www.google.com')
        driver.implicitly_wait(30)

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi' + Keys.ENTER)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        driver.refresh()


        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reportes', report_name = 'automatic-navigation-report'))
