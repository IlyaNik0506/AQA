import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Инициализация драйвера (например, Chrome)
driver = webdriver.Chrome()

# Открытие страницы
driver.get("https://suninjuly.github.io/selects2.html")

# Выбор элементов по их XPath
elements = driver.find_elements(By.XPATH, "//span[@class='nowrap'][@id='num1' or @id='num2']")

# Получение текста из выбранных элементов
texts = [element.text for element in elements]
z = 0
for i in texts:
    z += int(i)
# print(z)

select = Select(driver.find_element(By.ID, "dropdown"))
select.select_by_value(f"{z}")

button = driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(10)
# Закрытие браузера
driver.quit()
