from selenium.webdriver.common.by import By
from .base_page import BasePage

class LastFmResultsPage(BasePage):
    ARTIST_LINK = (By.CLASS_NAME, "link-block-target")

    def press_link(self):
        self.click(self.ARTIST_LINK)