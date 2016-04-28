from unittest import TestCase
from selenium import webdriver
from page_objects import PageObjects


class FiveTestsCases(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.page = PageObjects(self.driver)
        self.page.open('http://2gis.ru/novosibirsk')
        self.page.search_bar.select_passage()

    def test_search_good_date_input(self):
        """Тест Кейс1:
            Проверка поиска указанного маршрута
            Предусловия:
            1. Доступ в интернет
            2. Перейти на сайте 2gis.ru/novosibirsk в firefox
            3. Выбрать пункт "Проезд"
            Шаги:
            1. Ввести в поле "Откуда" название/адрес реального объекта
            2. Ввести в поле "Куда" название/адрес реального объекта
            3. Нажать enter
            Ожидаемый результат: Маршрут найден
        """
        from_obj = "Площадь Кирова"
        to_obj = "Версаль"
        self.page.search_passage_bar.search(from_obj, to_obj)
        frame_result_text = self.page.frame_result_search_passage.get_public_transport_text()
        self.assertTrue(from_obj and to_obj in frame_result_text)

    def test_search_bad_date_input(self):
        """Тест Кейс2:
            Проверка поиска указанного маршрута
            Предусловия:
            1. Доступ в интернет
            2. Перейти на сайте 2gis.ru/novosibirsk в firefox
            3. Выбрать пункт "Проезд"
            Шаги:
            1. Ввести в поле "Откуда" название/адрес несуществующего объекта (Пример: апрпар)
            2. Ввести в поле "Куда" название/адрес несуществующего объекта (Пример: врпрпавп)
            3. Нажать enter
            Ожидаемый результат:
            Появилась панель: “Увы, невозможно построить такой маршрут”
        """
        from_obj = "алллаитл"
        to_obj = "лрдод"
        self.page.search_passage_bar.search(from_obj, to_obj)
        no_results_is_displayed = self.page.frame_result_search_passage.check_no_results_is_displayed()
        self.assertTrue(no_results_is_displayed)

    def test_search_map_click_date_input(self):
        """Тест Кейс3:
            Проверка поиска указанного маршрута кликом по карте
            Предусловия:
            1. Доступ в интернет
            2. Перейти на сайте 2gis.ru/novosibirsk в firefox
            3. Выбрать пункт "Проезд"
            Шаги:
            1. Приблизте карту, чтобы на ней появились объекты
            2. Кликните на первое место/объект откуда строить маршрут
            3. Кликните на второе место/объект куда строить маршрут
            Ожидаемый результат:
            Появилась панель: Маршрут найден
        """
        from_obj = "//img[@src='http://tile0.maps.2gis.com/tiles?x=47857&y=20719&z=16&v=1']"
        to_obj = "//img[@src='http://tile2.maps.2gis.com/tiles?x=47858&y=20720&z=16&v=1']"
        self.page.zoom_panel.zoom(5)
        self.page.map.search_passage_by_clicking_on_objects(from_obj, to_obj)
        passage_on_map_is_displayed = self.page.result_search_on_map.check_passage_is_displayed()
        self.assertTrue(passage_on_map_is_displayed)

    def test_search_from_different_objects(self):
        """Тест Кейс4:
            Проверка поиска указанного маршрута для вида транспорта "Автомобильный маршрут"
            Предусловия:
            1. Доступ в интернет
            2. Перейти на сайте 2gis.ru/novosibirsk в firefox
            3. Выбрать пункт "Проезд"
            Шаги:
            1.  Выбрать вид транспорта "Автомобильный маршрут"
            2.	Ввести в поле "Откуда" адрес реального здания
            3.	Ввести в поле "Куда" название реальной остановки (Пример: Телецентр Остановка)
            4.	Нажать кнопку "Найти"

            Ожидаемый результат: Указанный маршрут построен
        """
        from_obj = "Виктора Уса 9"
        to_obj = "Телецентр Остановка"
        self.page.search_passage_bar.select_car_route()
        self.page.search_passage_bar.search(from_obj, to_obj)
        frame_result_text = self.page.frame_result_search_passage.get_auto_transport_text()
        self.assertTrue(from_obj and to_obj in frame_result_text)

    def test_search_subway_option(self):
        """Тест Кейс5:
            Проверка поиска указанного маршрута от станции метро до станции метро
            Предусловия:
            1. Доступ в интернет
            2. Установленный браузер последней версии Google Chrome
            3. Перейти на сайте 2gis.ru/novosibirsk в firefox
            4. Выбрать пункт "Проезд"
            5. Выбрать вид транспорта Метро
            Шаги:
            1.	Ввести в поле "Откуда" название реальной станции метро (Пример: Студенческая)
            2.	Ввести в поле "Куда" название другой реальной станции метро (Пример: Площадь Маркса)
            3.	Нажать кнопку "Найти"
            Ожидаемый результат: Маршрут найден
        """
        from_obj = "Студенческая"
        to_obj = "Площадь Маркса"
        self.page.search_passage_bar.select_subway()
        self.page.search_passage_bar.search(from_obj, to_obj)
        frame_result_text = self.page.frame_result_search_passage.get_public_transport_text()
        self.assertTrue(from_obj and to_obj in frame_result_text)

    def tearDown(self):
        self.driver.quit()
