import time
import unittest
# from unittest import TestCase

from selenium import webdriver
# ++from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Keyboard(unittest.TestCase):

	USERNAME = (By.ID, "username")
	PASSWORD = (By.ID, "password")

	def setUp(self) -> None:
		self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		self.chrome.maximize_window()
		self.chrome.get("https://the-internet.herokuapp.com/login")
		self.chrome.implicitly_wait(2)

	def tearDown(self) -> None:
		self.chrome.quit()

	def test_various_keys(self):
		user = self.chrome.find_element(*self.USERNAME)
		password = self.chrome.find_element(*self.PASSWORD)
		user.send_keys("anton")
		# time.sleep(2)
		# user.clear()
		# user.send_keys("tmsmith")
		# time.sleep(2)
		user.send_keys(Keys.CONTROL, 'a')
		time.sleep(2)
		user.send_keys(Keys.BACKSPACE)
		# list = ['t','o','m','s','m','i','t','h']
		# for litera in list:
		# 	user.send_keys(litera)
		# 	time.sleep(1)
		user.send_keys("tomsmih")
		time.sleep(2)
		user.send_keys(Keys.ARROW_LEFT, 't')
		time.sleep(2)
