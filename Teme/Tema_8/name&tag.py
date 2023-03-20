import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
time.sleep(2)
chrome.get('https://the-internet.herokuapp.com/login')
time.sleep(2)
chrome.find_element(By.NAME, "username").send_keys('tomsmith')
time.sleep(2)
chrome.find_element(By.NAME, "password").send_keys('SuperSecretPassword!')
time.sleep(2)
chrome.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
chrome.find_elements(By.TAG_NAME, "a")[2].click()
time.sleep(2)
chrome.get('https://the-internet.herokuapp.com/forgot_password')
chrome.find_element(By.NAME, "email").send_keys('tomsmith@gmail.com')
time.sleep(2)
chrome.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
