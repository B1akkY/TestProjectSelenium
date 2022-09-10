from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


@pytest.fixture(scope="function")
def browser():
    print("\nStart the browser..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    time.sleep(10)
    print("\nQuit the browser..")
    browser.quit()


class TestAlert():
    @pytest.mark.smoke
    def test_alert_positive(self, browser):
        browser.get(link)
        browser.find_element(By.TAG_NAME, "button").submit()
        # browser.switch_to.alert.accept()
        x = browser.find_element(By.ID, "input_value")
        y = calc(int(x.text))
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.TAG_NAME, "button").submit()
        # Я вообще не понял, какого хера, но при прогоне alert тупо игнорится как таковой
