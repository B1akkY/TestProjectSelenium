from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import math
import pyperclip


link = "https://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    time.sleep(10)
    browser.quit()


class TestWindow():
    @pytest.mark.smoke
    def test_new_window(self, browser):
        browser.get(link)
        browser.find_element(By.TAG_NAME, "button").submit()
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        x = browser.find_element(By.ID, "input_value")
        y = calc(int(x.text))
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.TAG_NAME, "button").submit()
        result = browser.switch_to.alert.text
        pyperclip.copy(result.split(":")[1])

