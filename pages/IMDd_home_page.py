import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class IMDbHomePage(BasePage):
    SEARCH_INPUT = (By.ID, "suggestion-search")
    SEARCH_BTN = (By.ID, "suggestion-search-button")
    
    def search_title(self, title_name):
        self.click(self.SEARCH_INPUT)
        self.enter_text(self.SEARCH_INPUT, title_name) 
        self.click(self.SEARCH_BTN)