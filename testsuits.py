import unittest
import HTMLTestRunner
import os
from searchproducts import SearchTest
from homepagetests import TestHomePage



# get the directory path to the output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)

# create a test suite combining search_test and home_pages
smoke_test = unittest.TestSuite([search_test,home_page_tests])

# open the report file
outfile = open(dir + "\SmokeTestReport.html", 'w')

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    verbosity=2,
    title='Test Report',
    description='Smoke Tests'
)


# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_test)
outfile.close()