import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By



class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("http://demo.magentocommerce.com/")

    def test_search_field(self):
        # check search field
        self.assertTrue(self.is_element_present(By.XPATH, (".//*[@id='nav-main']/div/div[2]/div[1]/a[2]/i")))


    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of element
        :param how: By locator type
        :param what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True



if __name__ == '__main__':
    unittest.main()
