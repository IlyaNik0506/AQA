import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)

r = str(math.ceil(math.pow(math.pi, math.e)*10000))

res = browser.find_element(By.LINK_TEXT, f"{r}")
res.click()

name = browser.find_element(By.NAME, "first_name")
name.send_keys("Ilya")

last_name = browser.find_element(By.NAME, "last_name")
last_name.send_keys("Nikolaev")

city = browser.find_element(By.NAME,"firstname")
city.send_keys("Moscow")

country = browser.find_element(By.ID, "country")
country.send_keys("Russia")

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(40)