import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(3)
chrome.maximize_window()
time.sleep(3)
chrome.get('https://formy-project.herokuapp.com/form')
time.sleep(2)
chrome.find_element(By.ID, "first-name").send_keys('Codreanu')  # 1
time.sleep(2)
chrome.find_element(By.ID, "last-name").send_keys('Florentina')  # 2
time.sleep(2)
chrome.find_element(By.ID, "job-title").send_keys('Tester')  # 3
time.sleep(3)
chrome.find_element(By.ID, "radio-button-2").click()
time.sleep(2)
chrome.find_element(By.ID, "checkbox-2").click()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Submit").click()
time.sleep(2)
