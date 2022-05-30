from asyncore import write
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import math
from selenium.webdriver.common.alert import Alert

URL = 'http://suninjuly.github.io/selects2.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    s1 = browser.find_element(By.ID, 'num1')
    s2 = browser.find_element(By.ID, 'num2')
    sum = int(s1.text) + int(s2.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    browser.find_element(By.CLASS_NAME, 'btn' ).click()
    alert = Alert(browser)
    print(alert.text)
    Alert(browser).accept

