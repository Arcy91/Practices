from page_model import ReactFormPage
from Config.Configuration import get_pre_configured_chrome_driver

ERRORMESSAGES = {
    "name": "A name field is empty.",
    "phone": "Phone number is not long enough.",
    "mail": "Email is in the wrong format."
}

page = ReactFormPage(get_pre_configured_chrome_driver())
page.open()

#TC 1 ures mező
page.submit_button().click()
alert = page.alert_popup()

assert ERRORMESSAGES["name"] == alert.text

alert.accept()

# TC 2
page.input_first_name().send_keys("Zoltán")
page.input_last_name().send_keys("Nagy")

page.submit_button().click()
alert = page.alert_popup()

assert ERRORMESSAGES["phone"] == alert.text

alert.accept()

# TC 3
page.input_first_name().clear()
page.input_first_name().send_keys("Zoltán")
page.input_last_name().send_keys("Nagy")
page.input_phone().send_keys("2222222222")
page.submit_button().click()
alert = page.alert_popup()

assert ERRORMESSAGES["mail"] == alert.text

alert.accept()