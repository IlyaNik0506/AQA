import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.ID, "input_value")
    x_text = x.text
    # print(x_text)
    y = calc(x_text)
    # print(y)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(f'{y}')

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    but = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    but.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
