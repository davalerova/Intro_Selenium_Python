import unittest
import time

from pyunitreport import HTMLTestRunner

from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\daval\Desktop\Platzi\Curso de introduccion a Selenium con Python\Scripts\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')
        driver.implicitly_wait(30)

    def test_register_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        time.sleep(5)
        self.assertEqual(driver.title, 'Create New Customer Account' )

        firs_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(firs_name.is_enabled() and
                        last_name.is_enabled() and
                        middle_name.is_enabled() and
                        email_address.is_enabled() and
                        news_letter_subscription.is_enabled() and
                        password.is_enabled() and
                        confirm_password.is_enabled() and
                        submit_button.is_enabled())

        firs_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('test@gmail.com')
        news_letter_subscription.click()
        password.send_keys('******')
        confirm_password.send_keys('******')
        time.sleep(5)
        submit_button.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reportes', report_name = 'register-new-user-report'))
