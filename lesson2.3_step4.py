import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
