import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyunitreport import HTMLTestRunner

from selenium import webdriver

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\daval\Desktop\Platzi\Curso de introduccion a Selenium con Python\Scripts\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()
        driver.implicitly_wait(30)

    def test_dynamics_controls(self):
        driver = self.driver
        paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        paragraph_to_check_text = paragraph_to_check.text
        print(paragraph_to_check_text)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while paragraph_to_check_text != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            paragraph_to_check_text = paragraph_to_check.text
            driver.refresh()

        while not found:
            if paragraph_to_check_text == correct_text:
                tries += 1
                driver.refresh()
                found = True
        self.assertEqual(found, True)
        print(f"It took {tries} tries to find the typo")
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reportes', report_name = 'typos-report'))
