import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.parametrize("url",
                         ["https://stepik.org/lesson/236895/step/1",
                          "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1",
                          "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1",
                          "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1",
                          "https://stepik.org/lesson/236905/step/1"])
class TestMultipleURL():

    def test_multiple_url(self, browser, url):
        link = url
        browser.get(link)
        form = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        form.send_keys(answer)
        button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        reply = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))
        reply = reply.text
        assert reply == "Correct!", f"{reply} не соответствует 'Correct!'"

