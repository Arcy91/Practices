from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from Config.Configuration import get_pre_configured_chrome_driver


class SearchPage:
    def __init__(self, browser: Chrome):
        self.browser = browser
        self.url = "https://www.duckduckgo.com"

    def input_search(self):
        return self.browser.find_element(By.ID, "searchbox_input")

    def button_search(self):
        return self.browser.find_element(By.XPATH, '//button[@type="submit"]')

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        self.browser.close()
