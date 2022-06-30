import time
# import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Name")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Last Name")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("email@mail.ru")

    # Способ 1 - вбить руками
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys("C:/test/test.txt")

    # Способ 2 - задать с помощью переменных
    # current_dir = os.path.abspath(os.path.dirname("C:/test/"))    # в конце директории с файлом должен быть /
    # file_name = "test.txt"    # имя файла, который будем загружать на сайт
    # file_path = os.path.join(current_dir, file_name)  # собираем путь к файлу
    # element = browser.find_element(By.ID, "file")
    # element.send_keys(file_path) # отправляем файл

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
