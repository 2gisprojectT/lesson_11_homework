import unittest
from unittest import TestCase
from selenium import webdriver
from datetime import datetime, timedelta
from ddt import ddt, data
import locale
from login_page import LoginPage
from home_page import HomePage
from requests_page import RequestsPage
from request_download_page import RequestDownloadPage

@ddt
class DropboxTest(TestCase):
    def setUp(self):
        """
        Предусловие: зайти на сайт dropbox.com, аутентифицироваться
        """
        locale.setlocale(locale.LC_ALL, "russian")

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.page = LoginPage(self.driver)
        self.page.open("https://www.dropbox.com")
        self.page.head_panel.sign_in("testcase.dropbox@mail.ru", "projectT111")
        self.page = HomePage(self.driver)

    @data(["Т", None],
          ["Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французс", "Запросы файлов"])
    def test_create_request_pairwise_without_time_download(self, value):
        """
        Заголовок: Запрос без срока загрузки
        Шаги
            1. Перейти на страницу запросов файлов
            2. Нажать на кнопку "Запросить файлы"
            3. В поле "Какой файл вам нужен?" ввести наименование/описание файла
            4. В поле "В какой папке в вашем Dropbox следует разместить файлы?" задать указанную папку или не задавать (None)
            5. Нажать кнопку "Далее"
            6. В появившемся окне "Отправить запрос файла" скопировать ссылку и нажать кнопку "Готово"
        Проверки:
            1. На странице запросов файлов появился созданный запрос
            2. На странице п.3.6 отображен функционал загрузки созданного запроса
        """
        self.page.main_panel.requests()
        self.page = RequestsPage(self.driver)
        self.page.requests_grid.create_request()
        self.page.request_edit_form.set_file_name(value[0])
        if value[1] is not None:
            self.page.request_edit_form.set_folder(value[1])
        self.page.request_edit_form.save()
        link = self.page.request_share_form.get_link()
        self.page.request_share_form.done()

        self.page.requests_grid.edit_request(0)
        request_name = self.page.request_edit_form.get_file_name()
        self.page = RequestDownloadPage(self.driver)
        self.page.open(link)
        self.assertEqual(value[0], request_name)
        self.assertEqual(value[0], self.page.request_download_panel.get_title())

    @data(["Т", None],
          ["Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французс", "Запросы файлов"])
    def test_create_request_pairwise_time_download_present_day(self, value):
        """
        Заголовок: Запрос со сроком загрузки "текущая дата"
        Предусловие: Тест выполнить раньше 23:00
        Шаги
            1. Перейти на страницу запросов файлов
            2. Нажать на кнопку "Запросить файлы"
            3. В поле "Какой файл вам нужен?" ввести наименование/описание файла
            4. В поле "В какой папке в вашем Dropbox следует разместить файлы?" задать указанную папку или не задавать (None)
            5. Добавить срок загрузки: текущая дата, время 23:00
            6. Нажать кнопку "Далее"
            7. В появившемся окне "Отправить запрос файла" скопировать ссылку и нажать кнопку "Готово"
        Проверки:
            1. На странице запросов файлов появился созданный запрос
            2. На странице п.3.7 отображен функционал загрузки созданного запроса с указанным сроком загрузки(п.3.5)
        """
        deadline_day = datetime.today()
        deadline_time = '23:00'

        self.page.main_panel.requests()
        self.page = RequestsPage(self.driver)
        self.page.requests_grid.create_request()
        self.page.request_edit_form.set_file_name(value[0])
        if value[1] is not None:
            self.page.request_edit_form.set_folder(value[1])
        self.page.request_edit_form.set_deadline(deadline_day, deadline_time)
        self.page.request_edit_form.save()
        link = self.page.request_share_form.get_link()
        self.page.request_share_form.done()

        self.page.requests_grid.edit_request(0)
        request_name = self.page.request_edit_form.get_file_name()
        self.page = RequestDownloadPage(self.driver)
        self.page.open(link)
        self.assertEqual(value[0], request_name)
        self.assertEqual(value[0], self.page.request_download_panel.get_title())
        deadline = deadline_day.strftime('%B').lower() + " " + str(deadline_day.day) + ", " \
                        + str(deadline_day.year) + " " + deadline_time
        self.assertIn(deadline, self.page.request_download_header.get_deadline())

    @data(["Т", None, 1, "Никогда"],
          ["Т", "Запросы файлов", 30, "В течении одного дня"],
          ["Т", None, 365, "В течение двух дней"],
          ["Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французс", "Запросы файлов", 1, "В течение недели"],
          ["Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французс", None, 30, "В течение 30 дней"],
          ["Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французс", "Запросы файлов", 365, "Всегда"])
    def test_create_request_pairwise_overdue_download(self, value):
        """
        Заголовок: Запрос со сроком загрузки больше текущей даты и включенной опцией просроченных загрузок
        Шаги
            1. Перейти на страницу запросов файлов
            2. Нажать на кнопку "Запросить файлы"
            3. В поле "Какой файл вам нужен?" ввести наименование/описание файла
            4. В поле "В какой папке в вашем Dropbox следует разместить файлы?" задать указанную папку или не задавать (None)
            5. Добавить срок загрузки: дата из таблицы, время 11:00
            6. Добавить значение просроченных загрузок
            7. Нажать кнопку "Далее"
            8. В появившемся окне "Отправить запрос файла" скопировать ссылку и нажать кнопку "Готово"
        Проверки:
            1. На странице запросов файлов появился созданный запрос
            2. На странице п.3.8 отображен функционал загрузки созданного запроса с указанным сроком загрузки(п.3.5)
        """
        deadline_day = datetime.today() + timedelta(days=value[2])
        deadline_time = '11:00'

        self.page.main_panel.requests()
        self.page = RequestsPage(self.driver)
        self.page.requests_grid.create_request()
        self.page.request_edit_form.set_file_name(value[0])
        if value[1] is not None:
            self.page.request_edit_form.set_folder(value[1])
        self.page.request_edit_form.set_deadline(deadline_day, deadline_time)
        self.page.request_edit_form.set_deadline_overdue(value[3])
        self.page.request_edit_form.save()
        link = self.page.request_share_form.get_link()
        self.page.request_share_form.done()

        self.page.requests_grid.edit_request(0)
        request_name = self.page.request_edit_form.get_file_name()
        self.page = RequestDownloadPage(self.driver)
        self.page.open(link)
        self.assertEqual(value[0], request_name)
        self.assertEqual(value[0], self.page.request_download_panel.get_title())
        deadline = deadline_day.strftime('%B').lower() + " " + str(deadline_day.day) + ", " \
                        + str(deadline_day.year) + " " + deadline_time
        self.assertIn(deadline, self.page.request_download_header.get_deadline())

    @data(["Тест \ : ? * \" |", "Не допускаются угловые скобки, а также следующие символы: \ / : ? * \" |"],
          ["   ", "Введите тему вашего запроса файла."])
    def test_negative_create_request_invalid_name_notify(self, value):
        """
        Заголовок: Невалидное наименование запроса
        Шаги
            1. Перейти на страницу запросов файлов
            2. Нажать на кнопку "Запросить файлы"
            3. В поле "Какой файл вам нужен?" ввести наименование/описание файла
            4. Нажать кнопку "Далее"
        Проверки:
            1. Всплывает предупреждение пользователя
        """
        self.page.main_panel.requests()
        self.page = RequestsPage(self.driver)
        self.page.requests_grid.create_request()
        self.page.request_edit_form.set_file_name(value[0])
        self.page.request_edit_form.save()

        self.assertEqual(value[1], self.page.request_edit_form.get_notify())

    def test_negative_create_request_invalid_name_max_length(self):
        """
        Заголовок: Длина наименования запроса max+1
        Шаги
            1. Перейти на страницу запросов файлов
            2. Нажать на кнопку "Запросить файлы"
            3. В поле "Какой файл вам нужен?" ввести строку длиной 141
        Проверки:
            1. Последний символ из наименования файла не удается ввести
        """
        value = "Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французских булок, да выпей чаю. Съешь ещё этих мягких французсК"

        self.page.main_panel.requests()
        self.page = RequestsPage(self.driver)
        self.page.requests_grid.create_request()
        self.page.request_edit_form.set_file_name(value)

        request_name = self.page.request_edit_form.get_file_name()
        self.assertEqual(value[:140], request_name)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()