from asyncore import write
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
from selenium.webdriver.common.alert import Alert

URL = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.get(URL)
    ppl_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule") 
    ppl_check = ppl_radio.get_attribute("checked")
    print("value of ppl_radio: ", ppl_check)
    assert ppl_check is None, "Robot radio is not selected by default"

     
