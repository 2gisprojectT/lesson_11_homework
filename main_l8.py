import unittest
from login_page import LoginPage
from main_page import MainPage
from selenium import webdriver
from unittest import TestCase


class Test(TestCase):
    def setUp(self):
        """
        Начальные условия:
            1) Переходим на страницу mail.google.com
            2) Авторизируемся через логин и пароль
        """
        email = "2giskargapolovtest@gmail.com"
        passwd = "2GisKargapolovTestTest"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        login_page = LoginPage(self.driver)
        login_page.open("http://mail.google.com/")
        login_page.login_form.login(email, passwd)

    def test_no_exist(self):
        """
        Шаги воспроизведения:
            1)Ввести в форму поиска текст, которого нет в письмах ящика.
            2)Нажать Enter.
        Ожидаемый результат:
            Вывод сообщения о том, что писем с таким текстом в ящике не найдено.
        """
        search_text = "some_text"
        page = MainPage(self.driver)
        page.search_bar.search(search_text)
        self.assertIn("Писем не найдено.", page.page_source)

    def test_overflow(self):
        """
        Шаги воспроизведения:
            1)Ввести строку, превышающую максимальную допустимую длину.
            2)Нажать Enter.
        """
        search_text = "overflow" * 400
        page = MainPage(self.driver)
        page.search_bar.search(search_text)
        self.assertIn("Слишком длинный поисковый запрос. Сократите его.", page.page_source)

    def test_gramm_mistake(self):
        """
            Шаги воспроизведения:
                1)Ввести в форму поиска слово, с намеренной опечаткой (Н-р: молако).
                2)Нажать Enter.
            """
        search_text = "молако"
        page = MainPage(self.driver)
        page.search_bar.search(search_text)
        self.assertIn("Возможно, вы имели в виду:", page.page_source)

    def test_size_mistake(self):
        """
        Шаги воспроизведения:
                1)нажать на кнопку "Показать параметры поиска"
                1)Ввести в форму под названием "Размер" строку, содержащую буквы.
                2)Нажать Enter.
        ОжидаемыЙ результат: Сообщение "Неверный запрос поиска – возврат всех писем"
        """
        size = "some_text"
        page = MainPage(self.driver)
        page.search_bar.add_param_size(size)
        page.search_bar.search("")
        self.assertIn("Неверный запрос поиска – возврат всех писем", page.page_source)

    def test_from(self):
        """
        Шаги воспроизведения:
                1)нажать на кнопку "Показать параметры поиска"
                1)Ввести в форму под названием "От" значение "Gmail".
                2)Нажать Enter.
        ОжидаемыЙ результат: Вывод списка сообщений от Gmail.
        """
        page = MainPage(self.driver)
        from_ = "Gmail"
        page.search_bar.add_param_from(from_)
        page.search_bar.search("")
        self.assertIn("Команда Gmail", page.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
