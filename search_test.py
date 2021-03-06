import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\daval\Desktop\Platzi\Curso de introduccion a Selenium con Python\Scripts\chromedriver.exe")
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        #driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_fiel_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_fiel_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enable(self):
        button = self.driver.find_element_by_class_name("button")

    def test_search_banner_promos(self):
        banners_list = self.driver.find_element_by_class_name("promos")
        banners = banners_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a/font/font')

    def test_shopping_car(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reporte_search', report_name = 'search-report'))
