from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_pre_configured_chrome_driver () -> webdriver.Chrome:
    options = Options()
    options.add_experimental_option("detach",True)
    #options.add_argument("window-positon=0,0")
    options.add_argument("--lang=en")
    #options.add_argument("--lang=hu")
    #options.add_experimental_option("excludeSwitches",["enable-logging"])

    return webdriver.Chrome(options=options)

if __name__ == '__main__':

    browser = get_pre_configured_chrome_driver()
    browser.maximize_window()

    #browser.close()
