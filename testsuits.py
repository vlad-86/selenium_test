import unittest
from searchproducts import SearchTest
from homepagetests import TestHomePage



search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)

smoke_test = unittest.TestSuite([search_test,home_page_tests])

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_test)