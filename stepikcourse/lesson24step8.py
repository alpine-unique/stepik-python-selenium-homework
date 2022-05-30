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

URL = 'http://suninjuly.github.io/explicit_wait2.html'
lessonURL = 'https://stepik.org/lesson/181384/step/8'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(URL)
    wait = WebDriverWait(browser, 15)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), "$100"))
    browser.find_element(By.CSS_SELECTOR, '#book').click()
    x = (browser.find_element(By.CSS_SELECTOR, "#input_value")).text
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
    ## wait.until(EC.alert_is_present())
    alert = Alert(browser).text
    answer = (alert.split()[-1])
    print(answer)
    Alert(browser).accept
    send_answer(answer, lessonURL)