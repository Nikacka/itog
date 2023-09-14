from selenium.webdriver.common.by import By
from settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl import element_has_css_class
import time
import pytest
@pytest.mark.auth_phone
def test_auth_with_phone(driver):
   # проверяем что таб Телефон активен по умолчанию
   wait = WebDriverWait(driver, 10)
   element = wait.until(element_has_css_class((By.ID, 't-btn-tab-phone'), "rt-tab--active"))
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys('settings.valid_phone')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('settings.valid_password')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Голованова\nНика')
   )
   assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Голованова"
   assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Ника"
@pytest.mark.auth_mail
def test_auth_with_email(driver):
   # Нажимаем на таб Почта
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим почту
   driver.find_element(By.ID, 'username').send_keys('settings.valid_email')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('settings.valid_password')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Голованова\nНика')
   )
   assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Голованова"
   assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Ника"
@pytest.mark.parametrize("numbers", ['12345', 'numbers'], ids=['one digit', 'invalid format'])
def test_auth_phone_invalid_format(driver):
   # Вводим телефон
   driver.find_element(By.ID, 'numbers').send_keys('Settings.numbers')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('Settings.valid_password')
   # Проверяем текст ошибки
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.CLASS_NAME, 'rt-input-container__meta--error'), 'Неверный формат телефона')
   )
@pytest.mark.auth_phone
@pytest.mark.parametrize("phone", ['', '          '], ids=['empty', 'only blanks'])
def test_auth_phone_empty_phone(driver):
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys('settings.empty_phone')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('Settings.valid_password')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.ID, 'rt-input-container__meta--error'), 'Введите номер телефона')
   )
@pytest.mark.auth_phone
@pytest.mark.parametrize("phone", ['Settings.invalid_phone'], ids= ['wrong phone', 'invalid phone 11 number'])
def test_auth_phone_wrong_user_name(driver):
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys('Settings.invalid_phone')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('Settings.valid_password')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
   )
   # проверяем ссылка Забыл пароль оранжевая
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_phone
@pytest.mark.xfail
@pytest.mark.parametrize("settings.empty_password", [''], ids= ['empty', 'only blanks'])
def test_auth_phone_empty_pass(driver):
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys('settings.valid_phone')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('settings.empty_password')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.ID, 'rt-input-container__meta--error'), 'Введите пароль')
   )
@pytest.mark.auth_phone
@pytest.mark.parametrize("passw", ['12345'], ids= ['wrong password number', 'invalid password letters'])
def test_auth_phone_wrong_pass(driver):
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys('settings.valid_phone')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('settings.invalid_password')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
   )
   # проверяем ссылка Забыл пароль оранжевая
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))
@pytest.mark.auth_mail
@pytest.mark.parametrize("mail", ['invalid_email'], ids= ['wrong mail', 'invalid mail'])
def test_auth_mail_wrong_user_name(driver, mail):
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим почту
   driver.find_element(By.ID, 'username').send_keys('settings.invalid_email')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('Settings.valid_password')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
   )
   # проверяем ссылка Забыл пароль оранжевая
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))
@pytest.mark.auth_mail
@pytest.mark.parametrize("settings.empty_email", [''], ids= ['empty', 'only blanks'])
def test_auth_mail_empty_mail(driver, mail):
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим адрес
   driver.find_element(By.ID, 'username').send_keys('settings.empty_email')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys('Settings.valid_password')
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.ID, 'rt-input-container__meta--error'), 'Введите адрес, указанный при регистрации')
   )

@pytest.mark.auth_mail
@pytest.mark.parametrize("Settings.invalid_password", ['12345'], ids= ['wrong passord number'])
def test_auth_mail_wrong_pass(driver, passw):
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим почту
   driver.find_element(By.ID, 'username').send_keys(Settings.valid_email)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(Settings.invalid_password)
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
   )
   # проверяем ссылка Забыл пароль оранжевая
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))