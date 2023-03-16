import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com/")
chrome.find_element(By.LINK_TEXT, "Form Authentication").click()
lista_inputuri = chrome.find_elements(By.TAG_NAME, "input")
lista_inputuri[0].send_keys("tomsmith")
lista_inputuri[1].send_keys("SuperSecretPassword!")
time.sleep(2)
chrome.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
chrome.quit()
