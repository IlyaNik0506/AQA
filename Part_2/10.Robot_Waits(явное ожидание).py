import math
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Предположим, у нас есть форма, где пользователь должен ввести свой email
price = (By.ID, "price")

# Мы хотим дождаться, пока в поле ввода email появится текст "test@example.com"
try:
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(price, "$100"))
    button = browser.find_element(By.XPATH, '//button[@id="book"]').click()

    x = browser.find_element(By.ID, "input_value")
    x_text = x.text
    browser.find_element(By.ID, "answer").send_keys(f'{calc(x_text)}')
    button = browser.find_element(By.ID, "solve").click()
    time.sleep(15)
except TimeoutException:
    print("Текст не появился в элементе в течение ожидаемого времени.")

browser.quit()
