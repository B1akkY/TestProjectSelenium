import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import math

link = "https://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestWait():
    @pytest.mark.smoke
    def test_browser_wait(self, browser):
        browser.get(link)
        WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        browser.find_element(By.ID, "book").click()

    @pytest.mark.regression
    def test_math_captcha(self, browser):
        x = browser.find_element(By.ID, "input_value")
        y = calc(int(x.text))
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "solve").submit()
        result = browser.switch_to.alert.text
        pyperclip.copy(result.split(":")[1])

