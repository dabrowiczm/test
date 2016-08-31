import unittest
from selenium import webdriver


class CalcTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://google.pl")
        cls.driver.title

    def test_addition(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("2+2")
        self.search_field.submit()
        result = self.driver.find_element_by_id("cwos")
        self.assertEqual("4", result.text)


    def test_multiplication(self):
        self.driver.get("http://google.pl")
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("3*4")
        self.search_field.submit()
        result = self.driver.find_element_by_id("cwos")
        self.assertEqual("12", result.text)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()