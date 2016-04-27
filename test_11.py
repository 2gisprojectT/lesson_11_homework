import unittest
from unittest import TestCase

from selenium import webdriver
from sign_in_page import SignInPage
from register_page import RegisterPage
from register_google_email_page import RegisterGoogleEmailPage
from register_google_password_page import RegisterGooglePasswordPage
from register_google_request_page import RegisterGoogleRequestPage

class SeleniumTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        page = SignInPage(self.driver)
        page.open("https://www.dropbox.com/login?src=logout/")
        page.sign_in_form.switch_to_sign_up()


    def test_maximal_length(self):
        """
        Тест: Проверка ввода в поле Имя значения больше максимального граничного
        Шаги:
            1. Ввести в поле «Имя» строку длиной больше 100 символов
            2. Поле «Фамилия» оставить пустым
            3. В остальные обязательные для заполнения поля ввести корректные значения
            4. Нажать кнопку зарегистрироваться
        Ожидаемый результат:
            1. Над полем «Имя» высветится ошибка «Введите значение: менее 100 символов»
        """
        page = RegisterPage(self.driver)
        page.registration_form.registration('a'*105, "projectt@mail.ru", "password")
        error_message = page.registration_form.get_error_message()
        self.assertEqual(error_message, "Введите значение: менее 100 символов.")

    def test_hint_easy_password(self):
        """
        Тест: Проверка подсказки к вводу слабого пароля
        Шаги:
            1. В обязательные для заполнения поля ввести корректные значения
            2. В поле «Пароль» ввести строку длиной 10 символов, состоящую из цифр
            3. Нажать на иконку сложности пароля
        Ожидаемый результат:
            1. Во всплывающем окне подсказки написано "Слабый"
        """
        page = RegisterPage(self.driver)
        page.password_field.input_password(10*'5')
        hint_message = page.password_field.get_hint()
        self.assertEqual(hint_message, "Слабый")

    def test_captcha_information(self):
        """
        Тест: Проверка выдачи информации о капче
        Шаги:
            1. В обязательные для заполнения поля ввести корректные значения
            2. Отметить галочку «Я принимаю Условия обслуживания Dropbox»
            3. Нажать кнопку "Зарегистрироваться"
            4. В появившейся форме с капчей нажать кнопку с вопросительным знаком
        Ожидаемый результат:
            1. Открылась новая вкладка с информацией о капче
        """
        page = RegisterPage(self.driver)
        page.registration_form.registration("login", "projectt@mail.ru", "password")
        page.captcha_form.info_about_captcha()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.assertEqual("reCAPTCHA Help", self.driver.title)

    def test_go_to_sign_in(self):
        """
        Тест: Проверка перенаправления на окно входа в уже существующий аккаунт
        Шаги:
            1. Ввести в поле «e-mail» уже зарегистрированный адрес электронной почты
            2. В остальные обязательные для заполнения поля ввести корректные значения
            3. Отметить галочку «Я принимаю Условия обслуживания Dropbox»
            4. Нажать кнопку зарегистрироваться
            5. Перейти по появившейся ссылке "Ввойдите в систему"
        Ожидаемый результат:
            1. Откроется окно для входа в существующий аккаунт
        """
        page = RegisterPage(self.driver)
        page.registration_form.registration("login", "user@mail.ru", "password")
        page.registration_form.go_to_sign_in()
        page = SignInPage(self.driver)
        header_text = page.sign_in_form.get_header_text()
        self.assertEqual("Войти", header_text)

    def test_register_with_google(self):
        """
        Тест: Проверка регистрации через Google
        Шаги:
            1. Нажать кнопку "Зарегистрироваться через Google"
            2. В открывшемся окне авторизации в поле для электронной почты ввести верный адрес электронной почты
            3. Нажать кнопку "Далее"
            4. В открывшейся вкладке в поле ввода пароля ввести верный пароль
            5. Нажать кнопку "Войти"
        Ожидаемый результат:
            1. В открывшемся окне произошла авторизация в введенный аккаунт
        """
        google_login = "alisaani95"
        page = RegisterPage(self.driver)
        page.registration_form.register_google()
        page = RegisterGoogleEmailPage(self.driver)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        page.google_email_form.input_email(google_login)
        page = RegisterGooglePasswordPage(self.driver)
        page.google_password_form.input_password("backspace011")
        page = RegisterGoogleRequestPage(self.driver)
        account_name = page.google_request_form.get_account_name()
        self.assertEqual(str(google_login) + "@gmail.com", account_name)

    def tearDown(self):
       self.driver.quit()

if __name__ == '__main__':
    unittest.main()
