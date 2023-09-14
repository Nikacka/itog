import os

from dotenv import load_dotenv

load_dotenv()



class Settings:

    base_url = 'https://b2c.passport.rt.ru'
    valid_email = 'kovtun221@gmail.com'
    valid_password = '84997341454Na'
    valid_phone = '89151307965'
    invalid_phone = '8193635278987'
    valid_email_for_reg = 'oubob@mailto.plus' #временный адрес для теста
    invalid_email = 'kovtun@gmail.ru'
    invalid_password = '12345'
    empty_email = ''
    empty_password = ''
    empty_phone = '    '
    menu_of_type_auth = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
    placeholder_name_of_user = ['Мобильный телефон', 'Электронная почта', 'Логин', 'Лицевой счёт']
    f_name = 'Ника'
    l_name = 'Ко'
    f_name_ = '-'
    l_name_ = '-'
    russian_generate_string = 'йцукен'
    latin_generate_string = 'qwertyu'
    chinese_chars = '我语'
    special_chars = '!@#${}$*****%^&*(#)_+_+=//\[\}]]]'
    numbers = 12345
    empty = ''
    passw1 = 'Qw987654321qw'
    passw2 = 'Uid125777nklP89683'
    passw3 = 'IOdd9876543210ELo8964776'


def valid_phone():
    return None