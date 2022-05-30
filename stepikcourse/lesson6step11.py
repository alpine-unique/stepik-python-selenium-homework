from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "http://suninjuly.github.io/registration1.html"

with webdriver.Chrome() as browser:
    browser.get(URL)
    element = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located)
    browser.find_element(By.XPATH, '//input[@placeholder="Input your name"]').send_keys('any value')
    browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('anyvalue@gmail.com')
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    test = browser.find_element(By.TAG_NAME, "h1")
    assert test.text == "Congratulations! You have successfully registered!"