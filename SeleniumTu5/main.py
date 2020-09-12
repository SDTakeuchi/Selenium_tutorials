import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):  
    def setUp(self):
        PATH = "C:/chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.python.org")

#-------------------------------------

    # def test_example(self):
    #     print ("Test")
    #     assert True

    # def test_example2(self):
    #     assert True
 
    #how this works is... setUp => test_example => tearDown => setUp => test_example2 => tearDown
    #note that it is not... setUp => test_example => test_example2 => tearDown, it always freshes

#-------------------------------------

    # def test_title(self):
    #     mainPage = page.MainPage()
    #     assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()