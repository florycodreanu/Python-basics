# import unittest
import time

import softest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


class Login(softest.TestCase):
    FORM_AUTHENTICATION_LINK = (By.XPATH, '//a[@href="/login"]')
    H2_ELEMENT = (By.XPATH, '//h2')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    HREF_LINK = (By.XPATH, '//a[text()="Elemental Selenium"]')
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    ERROR_MESSAGE_1 = (By.XPATH, '//div[@id="flash"]')
    ERROR_MESSAGE_2 = (By.XPATH, '//div[@id="flash"][(contains(text(),"Your username is invalid"))]')
    ERROR_CLOSED = (By.XPATH, '//a[@class="close"]')
    LABEL_LIST = (By.XPATH, '//label')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="flash success"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    ELEM_H4 = (By.TAG_NAME, 'h4')

    def setUp(self):
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.quit()

    # Test 1-Verificare daca noul url este corect
    def test_1_url(self):
        new_url = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.soft_assert(self.assertEqual, expected, new_url, 'URL-ul nu este corect')

    # Test 2 - Verificare page title e corect
    def test_2_head(self):
        h_title = self.chrome.title
        expected = 'The Internet'
        self.soft_assert(self.assertEqual, expected, h_title,  f'Error: Expected: {expected} Actual: {h_title}')

    # Test 3 - Verificare element xpath=//h2 este corect
    def test_3_element(self):
        actual = self.chrome.find_element(*self.H2_ELEMENT).text
        expected = 'Login Page'
        self.soft_assert(self.assertEqual, actual, expected, f'Error: Expected: {expected} Actual: {actual}')

    # Test 4 - Verificare Login button
    def test_4_login_displayed(self):
        button = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.soft_assert(self.assertTrue, button.is_displayed(), 'Butonul de LOGIN nu este vizibil')

    # Test 5 - Verificare href link
    def test_5_href(self):
        actual_link = self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        self.soft_assert(self.assertEqual, actual_link, 'http://elementalselenium.com/', 'Link-ul este gresit')

    # Test 6 - Verificare eroare user/pass goale
    def test_6_error_displayed(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 5).until(ec.presence_of_element_located(self.ERROR_MESSAGE_1))
        self.soft_assert(self.assertTrue, error.is_displayed(), 'Eroarea nu e vizibila')

    # Test 7 - Verificare mesaj eroare user si pass incorecte
    def test_7_mesaj_eroare(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tom')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecret!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE_2).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    # Test 8 - Verificare inchidere mesaj eroare
    def test_8_inchidere_mesaj_eroare(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(5)
        self.chrome.find_element(*self.ERROR_CLOSED).click()
        sleep(5)
        try:
            self.chrome.find_element(*self.ERROR_CLOSED)
        except NoSuchElementException:
            print("The text is not visible on the page! It's ok")

    # Test 9 - Verificare lista label
    def test_9_lista_label(self):
        elem_lista = self.chrome.find_elements(*self.LABEL_LIST)
        user = False
        password = False
        for t in elem_lista:
            if t.text == 'Username':
                user = True
            elif t.text == 'Password':
                password = True
        self.assertTrue(user, 'Textul Username nu se regaseste in lista')
        self.assertTrue(password, 'Textul Password nu se regaseste in lista')

    # Test 10 - Verificare elemente secure si flash succes
    def test_10_verif_secure(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        url_dupa_logare = self.chrome.current_url
        self.assertTrue("secure" in url_dupa_logare, 'Noul url nu contine secure')
        WebDriverWait(self.chrome, 10).until(ec.presence_of_element_located(self.SUCCESS_MESSAGE))
        message = self.chrome.find_element(*self.SUCCESS_MESSAGE)
        self.assertTrue(message.is_displayed(), 'Mesajul asteptat nu este afisat')
        self.assertTrue('secure area!' in message.text, 'Textul cautat nu se afla in mesajul afisat')

    # Test 11 - Verificare login - logout
    def test_11_verif_login_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        time.sleep(5)
        url_dupa_delogare = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(url_dupa_delogare, expected_url, f'Invalid url!Actual:{url_dupa_delogare}, Exp:{expected_url}')

    # Test 12 - Brute force password hacking
    def test_brute_force_pass(self):
        var_parole = self.chrome.find_element(*self.ELEM_H4).text.split()
        for password in var_parole:
            self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
            self.chrome.find_element(*self.PASSWORD).send_keys(password)
            self.chrome.find_element(*self.LOGIN_BUTTON).click()
            url = self.chrome.current_url
            if "secure" in url:
                print(f'Parola secreta este {password}')
                break
            else:
                print("Nu am reusit sa gasesc parola. Continuam cautarea")
        self.assertTrue('secure' in self.chrome.current_url, 'Nu am reusit sa gasesc parola')
