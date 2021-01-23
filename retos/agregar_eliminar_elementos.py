import unittest
import time
from selenium.webdriver.support.ui import Select

from pyunitreport import HTMLTestRunner

from selenium import webdriver

class EliminarAgregarElementos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\daval\Desktop\Platzi\Curso de introduccion a Selenium con Python\Scripts\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
        driver.implicitly_wait(30)

    def test_agregar_eliminar_elementos(self):
        driver = self.driver
        elements_added = int(input("How many elements will you add"))
        elements_remove = int(input("How many elements will you remove"))

        total_elements = elements_added - elements_remove

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        for i in range(elements_added):
            add_button.click()

        time.sleep(2)

        for i in range(elements_remove):
            try:
                remove_button = driver.find_element_by_class_name('added-manually')
                remove_button.click()
            except:
                print("No puede eliminar más elementos")
                break
        if total_elements > 0:
            print(f"There are {total_elements} elements")
        else:
            print("There are no elements")

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reportes', report_name = 'reto-agregar-eliminar-report'))
