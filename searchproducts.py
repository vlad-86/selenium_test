import selenium
from selenium import webdriver



# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()


# navigate to the application home page
driver.get("http://demo.magentocommerce.com/")


# get the search textbox
#search_field = driver.find_elements_by_css(".fa.fa-search")
search_field = driver.find_element_by_xpath(".//*[@id='nav-main']/div/div[2]/div[1]/a[2]/i")

search_field.click()

# enter search keyword and submit
search_field_extended = driver.find_element_by_id('edit-keys')
search_field_extended.clear()
search_field_extended.send_keys("phones")
search_field_extended.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_class_name("result-title")

# get the number of anchor elements found
print ("Found " + str(len(products)) + " products:")

# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print (product.text)

# close the browser window
driver.quit()