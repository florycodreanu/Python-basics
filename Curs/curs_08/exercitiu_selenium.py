import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/autocomplete")
chrome.find_element(By.ID, "autocomplete").send_keys("Ana")
time.sleep(5)
# chrome.find_element(By.XPATH,'//div[@class="pac-container hdpi"]/div/table/tr/td[2]/button').click()
chrome.find_element(By.CLASS_NAME, "dismissButton").click()
# chrome.find_element(By.XPATH,'//div[@class="pac-container hdpi"]/div/table/tr/td[2]/button').click()
