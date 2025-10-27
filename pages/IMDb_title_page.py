import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IMDbTitlePage(BasePage):
    TITLE =  (By.CLASS_NAME, "sc-cb6a22b2-0")
    RATING = (By.CLASS_NAME, "sc-4dc495c1-1")
    
    def get_title(self):
        return self.find_element(self.TITLE).text
    
    def get_rating(self):
        return self.find_element(self.RATING).text