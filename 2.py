from selenium.webdriver.common.by import By
from settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl import element_has_css_class
import time


def test_tab_auto_switch_phone_to_mail(driver):
   # проверяем что таб Телефон активен по умолчанию
   wait = WebDriverWait(driver, 10)
   element = wait.until(element_has_css_class((By.ID, 't-btn-tab-phone'), "rt-tab--active"))
   # Ввод почты
   driver.find_element(By.ID, 'username').send_keys('settings.valid_email')
   # Ввод пароля
   driver.find_element(By.ID, 'password').send_keys('settings.valid_password')
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
def test_tab_auto_switch_mail_to_phone(driver):
   # Нажимаем на таб Почта
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # Ввод номера
   driver.find_element(By.ID, 'username').send_keys('settings.valid_phone')
   # Ввод пароля
   driver.find_element(By.ID, 'password').send_keys('settings.valid_password')
   # проверяем что таб Телефон активен
   wait = WebDriverWait(driver, 10)
   element = wait.until(element_has_css_class((By.ID, 't-btn-tab-phone'), "rt-tab--active"))
def test_active_reg_ref(driver):
   # Ссылка на страницу регистрации
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.XPATH, '//a[@id="kc-register"]'), 'Зарегистрироваться')
   )
   # Ссылка активна
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'kc-register'), "rt-link--orange"))
   # Нажать на ссылку
   driver.find_element(By.ID, 'kc-register').click()
   # Проверить что открылась страница регистрации
   WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-right > div > div > h1'), 'Регистрация')
   )