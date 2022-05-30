from multiprocessing.connection import answer_challenge
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.common.alert import Alert
import os
from sender import send_answer

URL = "http://suninjuly.github.io/file_input.html"
lessonURL = "https://stepik.org/lesson/228249/step/8?unit=200781"

with webdriver.Chrome() as browser:
    browser.get(URL)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('123')
    browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('321')
    browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('112233@321.com')
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    alert = Alert(browser).text
    answer = (alert.split()[-1])
    print(answer)
    Alert(browser).accept
    send_answer(answer, lessonURL)
    

    