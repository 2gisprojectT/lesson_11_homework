from page_auth import PageAuth
from page_passwd import PagePasswd
from page_email import PageEmail
from page_request import PageRequest
from selenium import webdriver
import unittest

class auto_test_gmail(unittest.TestCase):

    def setUp(self):
        """
           Предусловие:
           1.Зайти на страницу регистрации mail.google.com
           2.Заполнить поля "Имя" и "Фамилия" валидными значениями.
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.page = PageAuth(self.driver)
        self.page.open("https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default")
        self.page.input_form.input_name('Петя')
        self.page.input_form.input_lastname('Иванов')


    def test_email_only_numbers(self):
        """
           Тест кейс "Проверка вывода ошибки при вводе в поле email больше 8 цифр"
           Шаги:
            1.Ввести в поле "Имя пользователя" строку из 9-ти символов, полностью состоящую из цифр.
            2.Нажать кнопку "Далее".
           Ожидание:
            Внизу поля "Имя пользователя" появляется надпись "Имя пользователя, состоящее из 8 или более символов, должно включать хотя бы одну латинскую букву (a-z)"
        """
        self.page_email = PageEmail(self.driver)
        self.page_request = PageRequest(self.driver)
        self.page_email.input_email.get_email('123456789')
        self.page_request.input_request.submit_button()
        error_msg = self.page_email.input_email.get_error_email()
        self.assertEqual(error_msg,"Имя пользователя, состоящее из 8 или более символов, должно включать хотя бы одну латинскую букву (a-z)")

    def test_min_email(self):
        """
           Тест кейс "Проверка вывода ошибки при вводе в поле email строки, меньше минимально возможной"
           Шаги:
            1.Ввод любых 5-ти символов в поле "Имя пользователя".
            2.Нажать кнопку "Далее".
           Ожидание:
            Внизу поля "Имя пользователя" появляется надпись "Допустимое количество символов: 6–30"
        """
        self.page_email = PageEmail(self.driver)
        self.page_request = PageRequest(self.driver)
        self.page_email.input_email.get_email('qwert')
        self.page_request.input_request.submit_button()
        error_msg = self.page_email.input_email.get_error_email()
        self.assertEqual(error_msg,"Допустимое количество символов: 6–30.")

    def test_max_length_passwd(self):
        """
           Тест кейс "Проверка вывода ошибки при вводе в поле "Пароль" строки, больше максимально возможной"
            Шаги:
             1.Ввести в поле "Пароль" строку, состоящую из 101 символа
             2.Нажать кнопку "Далее".
            Ожидание:
            Внизу поля "Пароль" появляется надпись "Должно быть не более 100 символов"

        """
        self.page_passwd = PagePasswd(self.driver)
        self.page_email = PageEmail(self.driver)
        self.page_request = PageRequest(self.driver)
        self.page_email.input_email.get_email('petyaivanov0981')
        s = "a" * 101
        passwd = self.page_passwd.input_passwd.get_passwd(s)
        self.page_request.input_request.submit_button()
        error_msg = self.page_passwd.input_passwd.get_error_passwd()
        self.assertEqual(error_msg,"Должно быть не более 100 символов")

    def test_passwd_frequent(self):
        """
           Тест кейс "Проверка вывода ошибки при вводе в поле "Пароль" часто встречающейся комбинации символов"
            Шаги:
             1.Заполнить полt "Имя пользователя" валидным значением.
             2.Ввести в поле "Пароль" строку, состоящую из распространенной комбинации символов
             3.Нажать кнопку "Далее".
            Ожидание:
            Внизу поля "Пароль" появляется надпись "Этот пароль очень распространен. Защитите аккаунт от взлома – придумайте более сложный пароль."
        """
        self.page_passwd = PagePasswd(self.driver)
        self.page_email = PageEmail(self.driver)
        self.page_request = PageRequest(self.driver)
        self.page_email.input_email.get_email('petyaivanov0981')
        passwd = self.page_passwd.input_passwd.get_passwd("12345qwerty")
        self.page_request.input_request.submit_button()
        error_msg = self.page_passwd.input_passwd.get_error_passwd()
        self.assertEqual(error_msg,'Этот пароль очень распространен. Защитите аккаунт от взлома – придумайте более сложный пароль.')

    def test_captcha(self):
      """
           Тест кейс "Проверка исчезновения картинки с капчей при отметке чекбокса "Пропустить проверку на робота" "
            Шаги:
             1. Убедиться что на форме есть картинка с капчей
             2. Отметить чекбокс "Пропустить проверку на робота. Может потребоваться проверка по телефону."
            Ожидание:
             Исчезает картинка с капчей, проверка на робота на данном этапе считается успешной.
      """
      self.captcha = self.page.input_form.get_captcha()
      self.assertTrue(self.captcha)
      check = self.page.input_form.check_captcha()
      self.captcha = self.page.input_form.get_captcha()
      self.assertFalse(self.captcha)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main();