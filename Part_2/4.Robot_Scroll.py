import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.ID, "input_value")
x_txt = x.text
t = browser.find_element(By.ID, "answer")
t.send_keys(f"{calc(x_txt)}")

check = browser.find_element(By.XPATH, "//label[@class='form-check-label' and @for='robotCheckbox']").click()
# time.sleep(5)
rule = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
rule.click()
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)