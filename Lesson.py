import pytest
from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLesson():

    def test_math_e2e_check(self, browser):
        browser.get(link)
        # проверяем ввод формулы в поле answer
        x_element = browser.find_element(By.ID, "input_value")
        x = int(x_element.text)
        y = calc(x)
        answer = browser.find_element(By.ID, "answer")
        answer.click()
        answer.send_keys(y)
        checkbox = browser.find_element(By.ID, "robotCheckbox")
        checkbox.click()
        assert checkbox.is_selected()
        radiobutton = browser.find_element(By.ID, "robotsRule")
        radiobutton.click()
        assert radiobutton.is_selected()
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

    @pytest.mark.smoke
    def test_checked_radiobutton(self, browser):
        browser.get(link)
        # проверяем значение атрибута checked у people_radio
        people_radio = browser.find_element(By.ID, "peopleRule")
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert people_checked is not None, "People radio is not selected by default"

    def test_checked_radiobutton2(self, browser):
        browser.get(link)
        # проверяем значение атрибута checked у robots_radio
        robots_radio = browser.find_element(By.ID, "robotsRule")
        robots_checked = robots_radio.get_attribute("checked")
        print("value of robots_radio: ", robots_checked)
        assert robots_checked is None

    def test_submit_disabled(self, browser):
        browser.get(link)
        # проверяем значение атрибута disabled у кнопки Submit
        button = browser.find_element(By.CSS_SELECTOR, '.btn')
        button_disabled = button.get_attribute("disabled")
        print("value of button Submit: ", button_disabled)
        assert button_disabled is None

    def test_submit_disabled_post_timeout(self, browser):
        browser.get(link)
        # проверяем значение атрибута disabled у кнопки Submit после таймаута
        time.sleep(15)
        button = browser.find_element(By.CSS_SELECTOR, '.btn')
        button_disabled = button.get_attribute("disabled")
        print("value of button Submit after 10sec: ", button_disabled)
        assert button_disabled is not None

# не забываем оставить пустую строку в конце файла
