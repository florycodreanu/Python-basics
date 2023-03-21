"""
Elementele dintr-un  site web sunt identificabile prin intermdiul unui tag
Exemple de tag-uri:
- id
- span
- a (ancora)
- td (table data)
- tr (table row)
- ul (unordered list)
- ol (ordered list)
- li (list item)
- input
- h (h1,h2,h3,h4,h5,h6)
- div
- p (paragraf)

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(3)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")  # putem deschide un site
chrome.find_element(By.ID, "first-name").send_keys("Florentina")
chrome.find_element(By.ID, "last-name").send_keys("Codreanu")
time.sleep(10)
chrome.quit()  # inchide toata instanta browserului
# chrome.close() -> inchide un singur tab (cel activ) din instanta de browser
