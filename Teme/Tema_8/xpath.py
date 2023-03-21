import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
time.sleep(2)
chrome.get('https://formy-project.herokuapp.com/autocomplete')
time.sleep(2)

# 3 dupa atribut=valoare
chrome.find_element(By.XPATH, '//input[@class="form-control pac-target-input"]').send_keys('Zambilelor, 4, Bl.5 Sc C')
chrome.find_element(By.XPATH, '//input[@id="street_number"]').send_keys('Zambielor Nr. 4')
chrome.find_element(By.XPATH, '//input[@placeholder="Street address 2"]').send_keys('Route 68')
time.sleep(2)

# 3 DUPA TEXTUL DE PE ELEMENT
chrome.find_element(By.XPATH, '//a[text()="Formy"]').click()
time.sleep(2)
chrome.find_element(By.XPATH, '//li/a[text()="Checkbox"]').click()
time.sleep(2)
chrome.find_element(By.XPATH, '//a[text()="Formy"]').click()
time.sleep(2)

# 1 dupa textul pe care il contine
chrome.find_element(By.XPATH, '//li/a[contains(text(),"Compl")]').click()
time.sleep(2)

# 1 cu OR folosind |
chrome.find_element(By.XPATH, '//input[@id="first-name"] | //input[@placeholder="Enter first name"]').send_keys('Flori')
time.sleep(2)

# 1 cu *
chrome.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('Cojanu')
time.sleep(2)

# 1 folodsind (xpath)[1]
chrome.find_elements(By.XPATH, '//input[@type = "radio"]')[1].click()
time.sleep(2)

# 1 folosind parent
text = chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong').text
print(text)
time.sleep(2)

# 1 folosind frate
chrome.find_element(By.XPATH, '//div[@class="input-group"]/preceding-sibling::div[1]/input').send_keys('QA Tester')
chrome.find_element(By.XPATH, '//div[@class="input-group"]/following-sibling::div//input[@id="checkbox-2"]').click()
time.sleep(2)


def select_years(years_of_experience):
    year_dropdown = Select(chrome.find_element(By.ID, "select-menu"))
    year_dropdown.select_by_visible_text(years_of_experience)


select_years("2-4")
time.sleep(2)
