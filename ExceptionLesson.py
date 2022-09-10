import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/cats.html"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


class TestException():
    @pytest.mark.smoke
    def test_exception_handling(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "button")
