from ntpath import join
from unicodedata import digit
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random 
import string
from selenium.webdriver.common.alert import Alert

URL = "http://suninjuly.github.io/huge_form.html"


with webdriver.Chrome() as browser:
    browser.get(URL)
    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        lengthofword = 10
        wtf = ''.join(random.choices(string.ascii_uppercase + string.digits, k = lengthofword))
        element.send_keys(str(wtf))
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(5)
    alert = Alert(browser)
    print(alert.text)
    Alert(browser).accept