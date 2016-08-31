import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://google.pl")
        cls.driver.title

    def search_test(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("test")
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//*[@id='rso']//h3/a")
        self.assertEqual(10, len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()