from pages.basePage import BasePage
from selenium.webdriver.common.by import By


class SiteMapPage(BasePage):
    path: str = "/sitemap.xml"

    def open_sitemap(self):
        return self.browser.get(self.base_url + self.path)

    def get_all_folders(self) -> []:
        return self.browser.find_elements(By.CSS_SELECTOR, "loc")
