from asyncore import write
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
from selenium.webdriver.common.alert import Alert

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


URL = 'http://suninjuly.github.io/get_attribute.html'
with webdriver.Chrome() as browser:
    browser.get(URL)
    treasure = browser.find_element(By.ID, 'treasure')
    x = treasure.get_attribute('valuex')
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    alert = Alert(browser)
    print(alert.text)
    Alert(browser).accept

