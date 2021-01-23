import unittest
import time
from selenium.webdriver.support.ui import Select

from pyunitreport import HTMLTestRunner

from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\daval\Desktop\Platzi\Curso de introduccion a Selenium con Python\Scripts\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')
        driver.implicitly_wait(30)

    def test_compare_products_removal_alert(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element_by_class_name('link-compare').click()

        driver.find_element_by_link_text('Clear All').click()

        alerta = driver.switch_to.alert

        alert_text = alerta.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alerta.accept()

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reportes', report_name = 'compare-products-report'))
