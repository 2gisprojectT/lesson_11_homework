from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from Page import Page
from Page_booking import  Page_booking

class RightWork(TestCase):

    def setUp(self):
        """
        Предусловия:
        1.  Зайти на сайт www.onetwotrip.com
        """
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.page = Page(self.driver, self.wait)
        self.page.open("http://www.onetwotrip.com/")

    def tearDown(self):
        self.driver.quit()

    def test_WrongCities(self):
        """
         Шаги :
         1. Выбрать тип рейса "В одну сторону"
         2. В полях "Откуда" и "Куда" выставить одинаковые города
         3. В поле "Когда" выставить любую дату
         4. Нажать кнопку "Найти"

         Проверка:
         Появляется сообщение "Неверно задан маршрут. Совпадают пункты вылета и прилёта."
         """
        flight_info = self.page.inf_about_flight
        flight_info.one_direction()
        flight_info.from_to('Новосибирск', 'Новосибирск')
        flight_info.date_to()
        flight_info.button_find()
        self.assertEqual(flight_info.error, 'Неверно задан маршрут. Совпадают пункты вылета и прилёта.')

    def test_WrongDates(self):
        """
            Шаги :
            1. Выбрать тип рейса "Туда и обратно"
            2. В полях "Откуда" и "Куда" выставить разные города
            3. В поле "Туда" выставить любую дату
            4. В поле "Обратно" выбрать дату, раньше даты в поле "Туда"
            5. Нажать кнопку "Найти"

            Проверка:
            Появляется сообщение "Неверно заданы даты"
            """
        flight_info = self.page.inf_about_flight
        flight_info.two_directions()
        flight_info.from_to('Новосибирск','Екатеринбург')
        flight_info.date_to()
        flight_info.date_back()
        flight_info.button_find()
        self.assertEqual(flight_info.error, 'Неверно заданы даты')

    def test_Autorization(self):
        """
            Шаги :
            1. Открыть "Личный кабинет"
            2. Нажать на логотип Twitter
            3. В открывшемся окне ввести данные от аккаунта Twitter

            Проверка:
            Поле "Личный кабинет" замениться на идентификаторы пользователя из выбранной соц. сети
            """
        autorization = self.page.autorize
        autorization.personal_area()
        autorization.twitt_logo()
        autorization.input_inf('fedosovdn@mail.ru', 'ltdrbcexrb')
        autorization.check_name('fedosov0405')

    def test_WrongRegistration(self):
        """
            Шаги :
            1. Открыть "Личный кабинет"
            2. В поле "Электронная почта" ввести почту, ввести пароль в соответствующее поле,
            ввести отличный пароль от введенного ранее в поле "Повторить пароль"
            3. Нажать кнопку "Зарегистрироваться"

            Проверка:
            Окно регистрации активно(регистрация не прошла)
            """
        registration = self.page.autorize
        registration.personal_area()
        registration.input_reg('fedosovdn@mail.ru', 'bla_bla', 'bla_bla_bla')
        self.assertTrue(registration.active_form)

    def test_baby(self):
        """
                Шаги :
                1. Выбрать тип рейса "В одну сторону"
                2. В полях "Откуда" и "Куда" выставить разные города
                3. В поле "Когда" выставить любую дату
                4. Нажать кнопку "Найти"
                ________________________________________________________
                5. Открыть первый вариант рейса
    	        6. Вводим информацию пассажира (дата рожения: 04.04.2016), нажимаем alt+enter

                Проверка:
                Появляется сообщение "Количество младенцев в брони не должно превышать количество взрослых."
                """
        flight_info = self.page.inf_about_flight
        flight_info.one_direction()
        flight_info.from_to('Новосибирск', 'Екатеринбург')
        flight_info.date_to()
        flight_info.button_find()

        self.page_booking = Page_booking(self.driver, self.wait)
        choice_flight = self.page_booking.choose_flight
        choice_flight.chosing_flight()
        passenger = self.page_booking.inf_about_passenger
        passenger.passenger_inf('jsmith@mail.ru','Jonh','Smith','2849729785')
        self.assertEqual(passenger.error, 'Количество младенцев в брони не должно превышать количество взрослых.')
