from selenium import webdriver
from selenium.webdriver.common.keys import Keys



profile = webdriver.FirefoxProfile('c:/Users/user\AppData\Local\Mozilla\Firefox\Profiles\dnycs6g4.py_test')
driver = webdriver.Firefox(profile)
driver.get("http://demo.magentocommerce.com/")
driver.implicitly_wait(10)
# get the search textbox
search_icon = driver.find_element_by_xpath(".//*[@id='nav-main']/div/div[2]/div[1]/a[1]/i")
search_icon.click()

search_field =driver.find_element_by_xpath(".//*[@id='edit-keys']")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath(".//*[@id='gl-container']/div[2]/div/div[2]/ul/li[1]/div[1]/a")

# get the number of anchor elements found
print("Found " + str(len(products)) + " products:")

# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print(product.text)

# close the browser window
driver.quit()