import unittest
from page import Page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """
        Предусловия:
        1) Зайти на mail.google.com
        2) Авторизоваться
        3) Нажать на кнопку "Написать"
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.page = Page(self.driver)
        self.page.open("https://mail.google.com")
        self.page.element_name.fill("Email", "arch.step.inc@gmail.com")
        self.page.element_name.fill("Passwd", "TestinG1234")
        self.page.button.click("z0")

    def test_all_filled_fields(self):
        """
        Шаги:
        1) Заполнить поле "Получатели" в формате: ____@____.____
        2) Заполнить оставшиеся поля
        3) Нажать на кнопку "Отправить"

        Ожидаемый результат:
        Форма отправки закроется, через некоторое время в центре экрана появится сообщение об успешной доставке
        """
        self.page.element_name.fill("to", "arch.step.inc@gmail.com")
        self.page.element_name.fill("subjectbox", "Hello")
        self.page.element_class_name.fill("LW-avf", "Hello", Keys.TAB, Keys.ENTER)
        mes = self.page.element_class_name.wait_text("vh", "Письмо отправлено. Просмотреть сообщение")
        self.assertTrue(mes)

    def test_no_theme(self):
        """
        Шаги:
        1) Заполнить поле "Получатели" в формате: ____@____.____
        2) Поле "Тема" оставить пустым
        3) Заполнить поле "Тело письма"
        4) Нажать на кнопку "Отправить"

        Ожидаемый результат:
        Форма отправки закроется, через некоторое время в центре экрана появится сообщение об успешной доставке
        """
        self.page.element_name.fill("to", "arch.step.inc@gmail.com")
        self.page.element_class_name.fill("LW-avf", "Hello", Keys.TAB, Keys.ENTER)
        mes = self.page.element_class_name.wait_text("vh", "Письмо отправлено. Просмотреть сообщение")
        self.assertTrue(mes)

    def test_wrong_destination(self):
        """
        Шаги:
        1) Поле "Получатели" заполнить текстом, не являющегося адресом
        2) Заполнить поле "Тело письма"
        3) Нажать на кнопку "Отправить"

        Ожидаемый результат:
        Появится сообщение об ошибке
        """
        self.page.element_name.fill("to", "курлык")
        self.page.element_class_name.fill("LW-avf", "Hello", Keys.TAB, Keys.ENTER)
        mes = self.page.element_class_name.wait_text("Kj-JD-Jz", "Адрес курлык в поле Кому не распознан. Проверьте правильность ввода всех адресов.")
        self.assertTrue(mes)

    def test_no_receivers(self):
        """
        Шаги:
        1) Поле "Получатели" не заполнять
        2) Заполнить поле "Тело письма"
        3) Нажать на кнопку "Отправить"

        Ожидаемый результат:
        Появится сообщение об ошибке
        """
        self.page.element_class_name.fill("LW-avf", "Hello", Keys.TAB, Keys.ENTER)
        mes = self.page.element_class_name.wait_text("Kj-JD-Jz", "Укажите как минимум одного получателя.")
        self.assertTrue(mes)

    def test_dynamic_save(self):
        """
        Шаги:
        1) Заполнить любое поле (можно одним символом)
        2) Подождать пару секунд

        Ожидаемый результат:
        В нижней части формы отправки справа появится надпись: "Идет сохранение", а затем: "Сохранено".
        """
        self.page.element_name.fill("to", "а")
        mes = self.page.element_class_name.wait_text("aWQ", "Идет сохранение")
        self.assertTrue(mes)
        mes = self.page.element_class_name.wait_text("aWQ", "Сохранено")
        self.assertTrue(mes)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
