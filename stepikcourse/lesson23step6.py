from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.common.alert import Alert
import os
from sender import send_answer
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException

URL = 'http://suninjuly.github.io/redirect_accept.html'
lessonURL = 'https://stepik.org/lesson/184253/step/6'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(URL)
    browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary').click()
    next_window = browser.window_handles[1]
    browser.switch_to.window(next_window)
    x = (browser.find_element(By.CSS_SELECTOR, "#input_value")).text
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    alert1 = Alert(browser).text
    answer = (alert1.split()[-1])
    print(answer)
    Alert(browser).accept
    send_answer(answer, lessonURL)

