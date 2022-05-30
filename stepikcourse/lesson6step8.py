from lib2to3.pgen2 import driver
from operator import contains
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
URL = "http://suninjuly.github.io/find_xpath_form"

with webdriver.Chrome() as browser:
    browser.get(URL)
    form1 = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]' )
    form1.send_keys('form1filled')
    form2 = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    form2.send_keys('form2filled')
    form3 = browser.find_element(By.CSS_SELECTOR, '.city')
    form3.send_keys('form3filled')
    form4 = browser.find_element(By.CSS_SELECTOR, '#country')
    form4.send_keys('form4filled')
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    alert = Alert(browser)
    print(alert.text)
    Alert(browser).accept

    



