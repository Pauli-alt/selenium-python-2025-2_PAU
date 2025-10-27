import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IMDbResultPage(BasePage):
    TITLE_LINK = (By.CLASS_NAME, "ipc-metadata-list-summary-item__t")

    def press_link(self):
        self.click(self.TITLE_LINK)