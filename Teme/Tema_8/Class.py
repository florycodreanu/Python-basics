import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Chiar daca site-ul original este in araba, codul este scris in limba engleza.
Majoritataea elementelor fiind accesibile.
"""

chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
time.sleep(2)
chrome.get('https://phptravels.net/signup')
time.sleep(3)
formular = chrome.find_elements(By.CLASS_NAME, "form-control")
formular[0].send_keys('Flori')
formular[1].send_keys('Cojanu')
formular[2].send_keys('0756846566')
time.sleep(3)
