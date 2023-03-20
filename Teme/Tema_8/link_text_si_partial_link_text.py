import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
time.sleep(2)
chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.ID, 'cookie_stop').click()
time.sleep(3)
chrome.find_element(By.LINK_TEXT, "Checkboxes").click()  # 1
time.sleep(3)
chrome.back()
chrome.find_element(By.LINK_TEXT, "Dropdown").click()
time.sleep(3)
chrome.back()
chrome.find_element(By.LINK_TEXT, "Frames").click()
time.sleep(3)
chrome.back()
chrome.find_element(By.PARTIAL_LINK_TEXT, "Entry").click()
time.sleep(3)
chrome.back()
chrome.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
time.sleep(3)
chrome.back()
chrome.find_element(By.PARTIAL_LINK_TEXT, "Form").click()
