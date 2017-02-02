import unittest
from selenium import webdriver



class SearchTest(unittest.TestCase):
    def setUp(self):

        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com/")

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
    def tearDown(self):

        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
