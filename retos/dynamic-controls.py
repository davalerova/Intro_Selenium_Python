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
        driver.find_element_by_link_text('Dynamic Controls').click()
        driver.implicitly_wait(30)

    def test_dynamics_controls(self):
        driver = self.driver
        check_box = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        check_box.click()

        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        remove_add_button.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')))
        remove_add_button.click()

        text_area_enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        text_area_enable_disable_button.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('David Valero')
        text_area_enable_disable_button.click()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reportes', report_name = 'controles-dinamicos-reporte'))
