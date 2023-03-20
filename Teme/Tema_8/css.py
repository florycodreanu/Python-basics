import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
time.sleep(2)
chrome.get('https://formy-project.herokuapp.com/keypress')
time.sleep(3)
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder*="Enter"').send_keys('Cojanu ')
time.sleep(1)
chrome.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Flori')
time.sleep(1)
chrome.find_element(By.CSS_SELECTOR, '#button').click()
time.sleep(1)
