from page_model import SearchPage
from POM.Configuration import get_pre_configured_chrome_driver


page = SearchPage(get_pre_configured_chrome_driver())

page.open()

print("Page title: ", page.browser.title)

#page.close()

input_search = page.input_search()
button_search = page.button_search()

print(input_search.is_displayed())

input_search.send_keys("Monty Python")

button_search.click()
