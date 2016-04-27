import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from auth_page import Page


class TestGmailAuth(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.page = Page(self.driver)
        self.page.open("https://mail.google.com/")

    def wait_captcha_img(self, email):
        captcha = self.driver.find_element_by_id("captcha-img")
        while (True):
            email.send_keys("a")
            email.submit()
            if (captcha.is_displayed()):
                return True

    def test_email_captcha(self):
        """
        Название : Проверка появления поля капчи при вводе e-mail

        Шаги :
        1.Вводим неверные e-mail и подтверждаем ввод пока не появиться поле капчи

        Тест пройден:
        Появляется поле ввода капчи

        """
        driver = self.driver
        email = driver.find_element_by_name("Email")
        email.send_keys("sndb11")
        WebDriverWait(driver, 10).until(
            lambda s: self.wait_captcha_img(email)
        )

    def test_not_register_email(self):
        """
            Название : Проверка появления сообщения: Не удалось распознать адрес электронной почты.

            Шаги :
            1.Вводим не существующий e-mail
            2.Подтверждаем ввод

            Тест пройден:
            Появляется сообщение : Не удалось распознать адрес электронной почты.

            """

        a = Page(self.driver)
        a.email_form.enter_email("qewdasafdwqas341r")
        self.assertEqual(a.email_form.get_error(), "Не удалось распознать адрес электронной почты.")

    def test_not_valid_email(self):
        """
            Название : Проверка появления сообщения: "Введите адрес электронной почты."

            Шаги :
            1.Вводим не e-mail
            2.Подтверждаем ввод

            Тест пройден:
            Появляется сообщение : "Введите адрес электронной почты."

            """

        a = Page(self.driver)
        a.email_form.enter_email("sndb11@")
        self.assertEqual(a.email_form.get_error(), "Введите адрес электронной почты.")

    def test_long_email(self):
        """
            Название : Проверка ввода e-mail'а превыщающего допустимую длинну"

            Шаги :
            1.Вводим e-mail больше 200 знаков
            2.Подтверждаем ввод

            Тест пройден:
            Появляется сообщение : "Слишком длинный адрес электронной почты."

            """
        key = "a" * 201
        page = Page(self.driver)
        page.email_form.enter_email(key)
        self.assertEqual(page.email_form.get_error(), "Слишком длинный адрес электронной почты.")

    def test_long_passwd(self):
        """
            Название : Проверка ввода пароля превыщающего допустимую длинну"

            Шаги :
            1.Вводим пароля больше 200 знаков
            2.Подтверждаем ввод

            Тест пройден:
            Появляется сообщение : "Должно быть не более 200 символов"

            """
        page = Page(self.driver)
        page.email_form.enter_email("doctorvra4@gmail.com")
        key = "a" * 201
        page.passwd_form.enter_passw(key)
        self.assertEqual(page.passwd_form.get_error(), "Должно быть не более 200 символов")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
