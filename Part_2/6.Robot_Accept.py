import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"
browser.get(link)

browser.find_element(By.XPATH, '//button[@type="submit"]').click()
browser.switch_to.alert.accept()

x = browser.find_element(By.ID, "input_value")
x_text = x.text
browser.find_element(By.ID, "answer").send_keys(f'{calc(x_text)}')
button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(10)