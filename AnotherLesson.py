import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(12 * math.sin(x)))


@pytest.fixture(scope="function")
def browser():
    print("\nStart the browser..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    time.sleep(5)
    print("\nQuit the browser..")
    browser.quit()


class TestJSExecution():
    @pytest.mark.regression
    def test_js_execution(self, browser):
        browser.get(link)
        x_element = browser.find_element(By.ID, "input_value")
        x = int(x_element.text)
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)
        checkbutton = browser.find_element(By.ID, "robotCheckbox")
        browser.execute_script("return arguments[0].scrollIntoView(true);", checkbutton)
        checkbutton.click()
        radbutton = browser.find_element(By.ID, "robotsRule")
        browser.execute_script("return arguments[0].scrollIntoView(true);", radbutton)
        radbutton.click()
        button = browser.find_element(By.TAG_NAME, "button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.submit()

