from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Keyboard(unittest.TestCase):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_various_keys(self):
        user = self.chrome.find_element(*self.USERNAME)
        password = self.chrome.find_element(*self.PASSWORD)
        user.send_keys("Flori")
        sleep(2)
        user.clear()
        sleep(1)
        user.send_keys('tomsmi')
        sleep(2)
        user.send_keys(Keys.CONTROL, 'a')
        sleep(2)
        user.send_keys(Keys.BACKSPACE)
        user.send_keys("tomsmih")
        password.send_keys('SuperSecret')
        sleep(2)
