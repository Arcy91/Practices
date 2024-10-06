from general_model import General_page
from selenium.webdriver.common.by import By

class ReactFormPage (General_page):
    def __init__(self,browser):
        super().__init__(browser,"https://high-flyer.hu/selenium/react_form.html")
        self.browser = browser
    def input_first_name(self):
        return self.browser.find_element(By.NAME,"firstName")

    def input_last_name(self):
        return self.browser.find_element(By.NAME, "lastName")
    def input_phone(self):
        return self.browser.find_element(By.NAME, "phone")
    def input_email(self):
        return self.browser.find_element(By.XPATH, '//input[placeholder="Email Address"]')
    def submit_button(self):
        return self.browser.find_element(By.XPATH, '//button')

    def alert_popup(self):
        return self.browser.switch_to.alert


