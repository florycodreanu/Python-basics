# import unittest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class AuthenticationInFirefox(softest.TestCase):
	USERNAME = 'admin'
	PASSWORD = 'admin'
	LOGIN_CONFIRM_TEXT = (By.XPATH, "//div[@class='example']/p")

	def setUp(self) -> None:
		self.firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
		self.firefox.maximize_window()
		self.firefox.implicitly_wait(2)

	def tearDown(self) -> None:
		self.firefox.quit()

	def test_auth(self):
		self.firefox.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')
		expected_text = "Congratulations! You must have the proper credentials."
		actual_text = self.firefox.find_element(*self.LOGIN_CONFIRM_TEXT).text
		self.soft_assert(self.assertEqual, expected_text, actual_text, "Error, authentication not succeded")
