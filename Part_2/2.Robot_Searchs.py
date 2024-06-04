import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.ID, "treasure")
    x_value = x.get_attribute("valuex")
    # x_text = x_value.text
    print(x_value)
    y = calc(x_value)
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
