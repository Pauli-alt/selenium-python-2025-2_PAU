from selenium.webdriver.common.by import By
from .base_page import BasePage

class LastFmArtistPage(BasePage):
    LATEST_RELEASES = (By.CLASS_NAME, "artist-header-featured-items-item-date")

    def get_latest_releases(self):
        return self.find_element(self.LATEST_RELEASES).text