import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestCaptcha():

    def test_captcha(self, browser):
        browser.get(link)
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)
        answer = browser.find_element(By.ID, "answer")
        answer.send_keys(y)
        checkbox = browser.find_element(By.ID, "robotCheckbox")
        checkbox.click()
        assert checkbox.is_selected()
        radiobutton = browser.find_element(By.ID, "robotsRule")
        radiobutton.click()
        assert radiobutton.is_selected()
        submit = browser.find_element(By.TAG_NAME, "button")
        submit.click()
