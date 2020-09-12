from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

class GoButtonElement(BasePageElement):
    locator = "go"


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
    #object as an argument is recommended by selenium

class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return 'Python' in self.driver.title

    def click_go_button(self):
        element= self.driver.find_element(*MainPageLocators.GO_BUTTON) 
        #put " * " when you are NOT sure/determined to use how many 'numbers' are going to be used, like one time you want the sum of (1,2), and other times you want the sum of (1,3,5,7).
        element.click()

class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source