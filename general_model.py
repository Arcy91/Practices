from datetime import datetime

from selenium.webdriver import Chrome

class General_page():
    def __init__(self,browser : Chrome,url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        self.browser.close()

    def refresh(self):
        self.browser.refresh()

    def save_screen(self,path):
        filename = f"{self.browser.title}-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}"
        print(f"Screenshot attempt:{path}\\{filename}")
        if self.browser.save_screenshot(fr'{path}\{filename}'):
            print("Screenshot saved successfully")
        else:
            print("Screenshot failed.")

