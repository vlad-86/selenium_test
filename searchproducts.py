import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time



class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_category(self):

        # get the search textbox
        #search_field = driver.find_elements_by_css(".fa.fa-search")
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='nav-main']/div/div[2]/div[1]/a[2]/i")

        self.search_field.click()

        # enter search keyword and submit
        self.search_field_extended =self.driver.find_element_by_id('edit-keys')
        self.search_field_extended.clear()
        self.search_field_extended.send_keys("phones")
        self.search_field_extended.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_class_name("result-title")

        # get the number of anchor elements found
        #print ("Found " + str(len(products)) + " products:")
        self.assertEqual(20,len(products))

        # iterate through each anchor element and print the text that is
        # name of the product
        #for product in products:
        #    print (product.text)

    def test_search_by_name(self):
        # get the search textbox
        # search_field = driver.find_elements_by_css(".fa.fa-search")
        self.search_field = self.driver.find_element_by_xpath(".//*[@id='nav-main']/div/div[2]/div[1]/a[2]/i")

        self.search_field.click()
        time.sleep(5)

        # enter search keyword and submit
        self.search_field_extended = self.driver.find_element_by_id('edit-keys')
        self.search_field_extended.clear()
        self.search_field_extended.send_keys("salt shaker")
        time.sleep(6)
        self.search_field_extended.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        result = self.driver.find_element_by_class_name("result-snippet")

        # get the number of anchor elements found
        # print ("Found " + str(len(products)) + " products:")
        self.assertEqual('No results', result.text)

    @classmethod
    def tearDownClass(cls):

        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
