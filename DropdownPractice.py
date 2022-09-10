import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/selects1.html"


def calc(number1, number2):
    return str(number1 + number2)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()


class TestDropdown():

    @pytest.mark.smoke
    def test_dropdown(self, browser):
        browser.get(link)
        num1 = browser.find_element(By.ID, "num1")
        x = num1.text
        x = int(x)
        num2 = browser.find_element(By.ID, "num2")
        y = num2.text
        y = int(y)
        sum = calc(x, y)
        print(sum)
        drop_choice = browser.find_element(By.CSS_SELECTOR, f"[value='{sum}']")
        assert drop_choice.is_displayed()
        drop_choice.click()
        browser.find_element(By.TAG_NAME, "button").submit()
