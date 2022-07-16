import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    try:
        browser.find_element(By.CSS_SELECTOR, "add_to_basket_form > button")
    except NoSuchElementException:
        return "Button is missing"
