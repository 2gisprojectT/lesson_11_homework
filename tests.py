import unittest
from page import Page
from selenium import webdriver


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
        self.page.authorization.to_authorize("arch.step.inc@gmail.com", "TestinG1234")
        self.page.send_form.open_form()

    def test_all_filled_fields(self):
        """
        Шаги:
        1) Заполнить поле "Получатели" в формате: ____@____.____
        2) Заполнить оставшиеся поля
        3) Нажать на кнопку "Отправить"

        Ожидаемый результат:
        Форма отправки закроется, через некоторое время в центре экрана появится сообщение об успешной доставке
        """
        self.page.send_form.send_email("arch.step.inc@gmail.com", "Hello", "Hello")
        self.page.message_sending.check_success_message("Письмо отправлено. Просмотреть сообщение")

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
        self.page.send_form.send_email("arch.step.inc@gmail.com", "", "Hello")
        self.page.message_sending.check_success_message("Письмо отправлено. Просмотреть сообщение")

    def test_wrong_destination(self):
        """
        Шаги:
        1) Поле "Получатели" заполнить текстом, не являющегося адресом
        2) Заполнить поле "Тело письма"
        3) Нажать на кнопку "Отправить"

        Ожидаемый результат:
        Появится сообщение об ошибке
        """
        self.page.send_form.send_email("курлык", "Hello", "Hello")
        self.page.message_sending.check_error_message("Адрес курлык в поле Кому не распознан. Проверьте правильность ввода всех адресов.")

    def test_no_receivers(self):
        """
        Шаги:
        1) Поле "Получатели" не заполнять
        2) Заполнить поле "Тело письма"
        3) Нажать на кнопку "Отправить"

        Ожидаемый результат:
        Появится сообщение об ошибке
        """
        self.page.send_form.send_email("", "Hello", "Hello")
        self.page.message_sending.check_error_message("Укажите как минимум одного получателя.")

    def test_dynamic_save(self):
        """
        Шаги:
        1) Заполнить любое поле (можно одним символом)
        2) Подождать пару секунд

        Ожидаемый результат:
        В нижней части формы отправки справа появится надпись: "Идет сохранение", а затем: "Сохранено".
        """
        self.page.send_form.fill_body_field("just one moment...")
        self.page.message_sending.check_save("Идет сохранение")
        self.page.message_sending.check_save("Сохранено")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
