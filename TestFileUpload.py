from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import os

link = "https://suninjuly.github.io/file_input.html"


@pytest.fixture(scope="function")
def browser():
    print("\nStart the browser..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    time.sleep(10)
    print("\nQuit the browser..")
    browser.quit()


class TestFileUpload():
    @pytest.mark.smoke
    def test_file_upload_positive(self, browser):
        browser.get(link)
        browser.find_element(By.NAME, "firstname").send_keys("Danya")
        browser.find_element(By.NAME, "lastname").send_keys("Yurin")
        browser.find_element(By.NAME, "email").send_keys("example@gmail.com")
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, "Ошибки.txt")
        browser.find_element(By.ID, "file").send_keys(file_path)
        browser.find_element(By.TAG_NAME, "button").submit()

