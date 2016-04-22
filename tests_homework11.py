import unittest
from selenium import webdriver
from page_home import HomePage
from page_user_auth import UserAuthPage
from page_user_info import UserInfoPage


class OneTwoTripTests(unittest.TestCase):
    def setUp(self):
        """
        Инициализация драйвера для тестирования:
            [1] Открываем сайт.
            [2] Переходим в личный кабинет.
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        page = HomePage(self.driver)

        page.open("https://www.onetwotrip.com/ru/")
        page.top_panel.click_login()

    def test_incorrect_authorization(self):
        """
        Шаги воспроизведения:
            [1] В поле "Электронная почта" ввести почту зарегистрированную на onetwotrip.com.
            [2] В поле "Пароль" ввести произвольные буквы и цифры.
            [3] Кликнуть по кнопке "Войти".
        Ожидаемый результат:
            [*] Авторизация не проходит, ниже поля "пароль" появляется красное окошко, уведомляющая об ошибке.
        """
        page_auth = UserAuthPage(self.driver)

        page_auth.user_auth.authorization("antonprojectt@leeching.net", "abcd123")
        error_info = page_auth.user_auth.get_error()
        self.assertEqual(error_info, "Неправильный пароль или почта")

    def test_twitter_authorization(self):
        """
        Шаги воспроизведения:
            [1] Нажать на лого Twitter.
            [2] В открывшимся окне ввести данные от аккаунта Twitter.
            [3] Нажать кнопку "Войти".
        Ожидаемый результат:
            [*] Настройках профиля пользователя, в пункте "Авторизация" появится надпись "Twitter".
        """
        page_auth = UserAuthPage(self.driver)

        page_auth.user_auth.twitter_authorization("antonprojectt@leeching.net", "test009")
        auth_info = page_auth.user_auth.get_auth_info()
        self.assertEqual(auth_info, "АВТОРИЗАЦИЯ\nTwitter")

    def test_add_passenger_to_address_book(self):
        """
        Шаги воспроизведения:
            [1] Авторизироваться и перейти в свой профиль.
            [2] Кликнуть по кнопке "Добавить пассажира".
            [3] В поля ввести валидные значения.
            [4] Кликнуть по кнопке "Сохранить изменения".
            [5] Обновить страницу браузера.
        Ожидаемый результат:
            [*] Добавится новый пассажир, информация о пассажире соответствует ранее введеной.
        """
        page_user_info = UserInfoPage(self.driver)
        passenger_info = ("IVANOV", "IVAN", "12.12.2016", "123QWE", "12.12.2100")

        page_user_info.user_info.authorization_and_go_to_profile("antonprojectt@leeching.net", "test009")
        page_user_info.user_info.add_passenger(passenger_info)
        result = page_user_info.user_info.get_passenger_info()

        self.assertEqual(result[0], passenger_info[0])
        self.assertEqual(result[1], passenger_info[1])
        self.assertEqual(result[2], "12 дек 2016")
        self.assertEqual(result[3], passenger_info[3])
        self.assertEqual(result[4], passenger_info[4])

    def test_select_country(self):
        """
        Шаги воспроизведения:
            [1] Авторизироваться и перейти в свой профиль.
            [2] Выбрать страну в поле "Страна".
            [3] Кликнуть по кнопке "Сохранить изменения".
            [4] Обновить страницу.
        Ожидаемый результат:
            [*] В поле "Страна" отобразиться ранее выбранное значение.
        """
        page_user_info = UserInfoPage(self.driver)
        country_name = {"Венгрия": "HU"}

        page_user_info.user_info.authorization_and_go_to_profile("antonprojectt@leeching.net", "test009")
        page_user_info.user_info.change_country(country_name.get("Венгрия"))

        real_result = page_user_info.user_info.get_country_name()
        expected_result = country_name.get("Венгрия")

        self.assertEqual(real_result, expected_result)

    def test_change_password(self):
        """
        Шаги воспроизведения:
            [1] Авторизироваться и перейти в свой профиль.
            [2] Нажать "Сменить пароль".
            [3] В поле "Новый пароль" ввести новый пароль.
            [4] В поле "Повторите новый пароль" повторить ввод нового пароля.
            [5] Кликнуть по кнопке "Сохранить изменения".
        Ожидаемый результат:
            [*] Появится окошко с информацией о смене пароля.
        """
        page_user_info = UserInfoPage(self.driver)

        page_user_info.user_info.authorization_and_go_to_profile("antonprojectt@leeching.net", "test009")
        page_user_info.user_info.change_password("test123")

        info_field = page_user_info.user_info.get_element()
        result = page_user_info.user_info.get_change_password_info()

        self.assertTrue(info_field.is_displayed())
        self.assertEqual(result, "Изменение пароля")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
