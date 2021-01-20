import unittest

from pyunitreport import HTMLTestRunner

from selenium import webdriver

class HelloWord(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path =r'C:\Users\daval\Desktop\Platzi\Curso de introduccion a Selenium con Python\Scripts\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)


    def test_hello_word(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reportes', report_name = 'hello-word-report'))
