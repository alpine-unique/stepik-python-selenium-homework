from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.common.alert import Alert
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

URL = "https://SunInJuly.github.io/execute_script.html"

with webdriver.Chrome() as browser:
    browser.get(URL)
    browser.execute_script("window.scrollBy(0, 100);", )
    x = browser.find_element(By.ID, 'input_value')
    browser.find_element(By.ID, 'answer').send_keys(calc(x.text))
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    alert = Alert(browser)
    print(alert.text)
    Alert(browser).accept

    


    
    