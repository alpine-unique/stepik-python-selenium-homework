from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.common.alert import Alert

URL = "http://suninjuly.github.io/find_link_text"

with webdriver.Chrome() as browser:
    browser.get(URL)
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    form1 = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]' )
    form1.send_keys('form1filled')
    form2 = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    form2.send_keys('form2filled')
    form3 = browser.find_element(By.CSS_SELECTOR, '.city')
    form3.send_keys('form3filled')
    form4 = browser.find_element(By.CSS_SELECTOR, '#country')
    form4.send_keys('form4filled')
    button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    button.click()
    alert = Alert(browser)
    print(alert.text)
    Alert(browser).accept
    


    



