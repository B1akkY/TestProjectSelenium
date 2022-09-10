import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    valuex = x_element.get_attribute("valuex")
    print("valuex: ", valuex)
    x = valuex
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
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
