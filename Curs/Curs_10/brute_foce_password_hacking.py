import softest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class PasswordCheck(softest.TestCase):
	TEXT_TO_BE_EVALUATED = (By.CSS_SELECTOR, "h4")
	USERNAME = (By.ID, "username")
	PASSWORD = (By.ID, "password")
	LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
	SECURE_AREA = (By.XPATH, "//h2")

	def setUp(self) -> None:
		self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		self.chrome.maximize_window()
		self.chrome.get("https://the-internet.herokuapp.com/login")
		self.chrome.implicitly_wait(2)

	def tearDown(self) -> None:
		self.chrome.quit()

	def test_brute_force_password_hacking(self):
		text_extracted_for_evaluation = self.chrome.find_element(*self.TEXT_TO_BE_EVALUATED).text.split()
		logged_in = False
		for i in range(len(text_extracted_for_evaluation)):
			self.chrome.find_element(*self.USERNAME).send_keys("tomsmith")
			self.chrome.find_element(*self.PASSWORD).send_keys(text_extracted_for_evaluation[i])
			self.chrome.find_element(*self.LOGIN_BUTTON).click()
			login_confirmation = self.chrome.find_element(*self.SECURE_AREA).text
			if login_confirmation == "Secure Area":
				logged_in = True
				print(f"The password was found and it is {text_extracted_for_evaluation[i]}")
				break
		self.soft_assert(self.assertTrue, logged_in, "Error: the password could not be hacked")
