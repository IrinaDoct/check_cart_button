from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_exist_product(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    button = None
    try:
        button = browser.find_element_by_css_selector('button.btn-add-to-basket')
    except:
        print("\nFind error")
    assert button != None, "Button 'add to basket' doesn't exist"