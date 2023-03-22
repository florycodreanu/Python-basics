from time import sleep
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class Firefox(softest.TestCase):
    form_link = (By.XPATH, '//a[@href="/login"]')
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    login_button = (By.XPATH, '//button[@type="submit"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="flash success"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    notification = (By.XPATH, '//*[@id="flash"]')

    def setUp(self) -> None:
        self.firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.firefox.maximize_window()
        self.firefox.implicitly_wait(10)
        self.firefox.get('https://the-internet.herokuapp.com')

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_correct_login(self):
        self.firefox.find_element(*self.form_link).click()
        sleep(2)
        self.firefox.find_element(*self.username).send_keys('tomsmith')
        sleep(1)
        self.firefox.find_element(*self.password).send_keys('SuperSecretPassword!')
        sleep(1)
        self.firefox.find_element(*self.login_button).click()
        message = self.firefox.find_element(*self.SUCCESS_MESSAGE)
        self.assertTrue(message.is_displayed(), 'Mesajul asteptat nu este afisat')

    def test_logout(self):
        self.firefox.find_element(*self.form_link).click()
        self.firefox.find_element(*self.username).send_keys('tomsmith')
        self.firefox.find_element(*self.password).send_keys('SuperSecretPassword!')
        self.firefox.find_element(*self.login_button).click()
        self.firefox.find_element(*self.LOGOUT_BUTTON).click()
        self.assertTrue(self.firefox.find_element(*self.username).is_displayed(), 'Eror delogarea nu s-a efectuat')

    def test_notification_message(self):
        self.firefox.find_element(By.XPATH, '//a[@href="/notification_message"]').click()
        message = self.firefox.find_element(*self.notification)
        self.soft_assert(self.assertTrue, message.is_displayed(), 'Error: Message not found!')
