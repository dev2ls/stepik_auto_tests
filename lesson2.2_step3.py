import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, "num1").text
y = browser.find_element(By.ID, "num2").text

summa = int(x) + int(y)
print(summa)

try:
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summa))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
