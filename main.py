from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
import unittest

from CreateEditForm import CreateEditForm
from PageLogin import PageLogin
from PageRequests import PageRequests


class Test(TestCase):
    """
    Предусловия:
        1) Зайти на сайт dropbox.com/request и аутентифицироваться
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        page_login = PageLogin(self.driver)
        page_login.open("https://www.dropbox.com/requests")
        email = "evgenijkatunov@mail.ru"
        passwd = "test123"
        page_login.login_form.login(email, passwd)

    def test_empty_name(self):
        """
        Тест: Создание запроса файлов с пустой темой
        Действия:
            1) Нажать на кнопку создания запроса
            2) Оставить поле темы запроса пустым
            3) Перейти на следующий шаг мастера
        Проверить:
            Появление сообщения о необходимости ввести тему запроса
        """

        page = PageRequests(self.driver)
        page.drops_management_grid.create_request()
        page.create_edit_form.next_step()
        error_msg = page.create_edit_form.get_error()
        self.assertEqual("Введите тему вашего запроса файла.", error_msg)

    def test_more_then_maxlen_name(self):
        """
        Тест: Создание запроса файлов с темой больше максимальной длины
        Действия:
            1) Нажать на кнопку создания запроса
            2) Заполнить поле темы максимально допустимым числом символов
            3) Пройти остальные шаги мастера со значениями по умолчанию
        Проверить:
            Создан запрос с обрезанным наименованием до 140 символов
        """

        name = "a" * 141;
        page = PageRequests(self.driver)
        page.drops_management_grid.create_request()
        page.create_edit_form.set_name(name)
        page.create_edit_form.next_step()
        page.share_request_form.done()
        page.refresh()
        page.drops_management_grid.show_request(0)
        name_request = page.create_edit_form.get_name()
        self.assertEqual(name[:140], name_request)

    def test_unresolved_symbol_name(self):
        """
        Тест:
            Создание запроса файлов с недопустимым символом в теме
        Действия:
            1) Нажать на кнопку создания запроса
            2) Ввести в поле темы строку с недопустимыми символами
        Проверить:
            Появление сообщения о вводе недопустимых символов
        """

        name = "test/test"
        page = PageRequests(self.driver)
        page.drops_management_grid.create_request()
        page.create_edit_form.set_name(name)
        error_msg = page.create_edit_form.get_error()
        self.assertEqual("В названиях запрещено использовать косую черточку (/). Пожалуйста, выберите другое название.",
                         error_msg)

    def test_overdue_downloads_never(self):
        """
        Тест:
            Создание запроса файлов с указанием срока просроченной загрузки "Никогда"
        Действия:
            1) Начать создавать запрос с корректной темой
            2) Выставить checkBox "Срок"
            3) Выбрать в поле просроченные загрузки: Никогда
            4) Пройти остальные шаги мастера со значениями по умолчанию
        Проверить:
            Создан запрос без периода просроченной загрузки
        """

        name = "TEST2"
        page = PageRequests(self.driver)
        page.drops_management_grid.create_request()
        page.create_edit_form.set_name(name)
        page.create_edit_form.set_deadline_flag(True)
        page.create_edit_form.set_after_deadline_download_period("Никогда")
        page.create_edit_form.next_step()
        page.share_request_form.done()
        page.refresh()
        page.drops_management_grid.show_request(0)
        name_request = page.create_edit_form.get_name()
        displayed = page.create_edit_form.is_displayed_after_deadline_upload_link()
        self.assertEqual(name, name_request)
        self.assertTrue(displayed)

    def test_overdue_downloads_notnever(self):
        """
        Тест:
            Создание запроса файлов с указанием срока просроченной загрузки отличным от "Никогда"
        Действия:
            1) Начать создавать запрос с корректным наименованием
            2) Выставить checkBox "Срок"
            3) Выбрать в поле просроченные загрузки: в течение одного дня
            4) Пройти остальные шаги мастера со значениями по умолчанию
        Проверить:
            Создан запрос с заданным сроком загрузки
        """

        name = "TEST3"
        page = PageRequests(self.driver)
        page.drops_management_grid.create_request()
        page.create_edit_form.set_name(name)
        page.create_edit_form.set_deadline_flag(True)
        page.create_edit_form.set_after_deadline_download_period("В течении одного дня")
        page.create_edit_form.next_step()
        page.share_request_form.done()
        page.refresh()
        page.drops_management_grid.show_request(0)
        name_request = page.create_edit_form.get_name()
        period = page.create_edit_form.get_after_deadline_download_period()
        self.assertEqual(name, name_request)
        self.assertEqual("В течении одного дня", period)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main();
