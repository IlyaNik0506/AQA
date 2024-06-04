import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

# browser.find_element(By.NAME,"firstname")
# browser.find_element(By.NAME,"lastname")
# browser.find_element(By.NAME,"email")
inp = browser.find_elements(By.XPATH,"//input[@type='text']")
for i in inp:
    i.send_keys("123")

path = "/Users/ilya_nikolaev/PycharmProjects/AQA/Part_2/1"

file = browser.find_element(By.ID, "file")
file.send_keys(f"{path}")
button = browser.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)