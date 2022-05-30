from asyncore import write
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
from selenium.webdriver.common.alert import Alert

URL = "http://suninjuly.github.io/math.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
with webdriver.Chrome() as browser:
    browser.get(URL)
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text   
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    alert = Alert(browser)
    print(alert.text)
    Alert(browser).accept



    
