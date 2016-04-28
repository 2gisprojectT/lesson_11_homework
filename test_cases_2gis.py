from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from page import Page


class SiteTestCase(TestCase):

    def setUp(self):
        """
            Начальные условия:
                1. Находиться на сайте 2gis.ru
        """
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver)
        self.driver.implicitly_wait(20)

        self.page = Page(self.driver, self.actions)
        self.page.open('https://2gis.ru')

    def test_click_district(self):
        """
            Test Case:
                Проверка отображения информации о Центральном округе по клику на карте
            Шаги:
                1. Кликнуть по любым координатам Центрального округа
            Ожидаемый результат:
                Появится карточка Центрального округа с соответствующим названием
        """
        self.page.map.click('Центральный округ')

        self.assertEqual(self.page.geo_card.title, 'Центральный округ')

    def test_click_object_with_zoom(self):
        """
            Test Case:
                Проверка отображения информации о Первомайском сквере после увеличения зума карты
            Шаги:
                1. Приблизить карту минимум 4 раза
                2. Кликнуть по любым координатам Первомайского сквера
            Ожидаемый результат:
                Появится карточка Первомайского сквера с соответствующим названием
        """
        self.page.scale_bar.increase(4)
        self.page.map.click('Первомайский сквер')

        self.assertEqual(self.page.geo_card.title, 'Первомайский сквер')

    def test_click_object_and_search(self):
        """
            Test Case:
                Сравнение информации карточки организации по клику на карте и после поиска
            Шаги:
                1. Приблизить карту минимум 4 раза
                2. Кликнуть по любым координатам Оперного театра
                3. В поисковой строке ввести: "Оперный театр"
                4. Кликнуть по первому результату поиска
            Ожидаемый результат:
                Название организации на карточке после поиска и на всплывающем окне совпадет
        """
        self.page.scale_bar.increase(4)
        self.page.map.click('Оперный театр')
        click_object_text = self.page.geo_card.title

        self.page.search_bar.search('Оперный театр')
        self.page.search_result.choose_first_result()

        self.assertEqual(('' + click_object_text).lower(), ('' + self.page.firm_card.title).lower())

    def test_click_object_and_near_stop(self):
        """
            Test Case:
                Проверка функции нахождения ближайшей станции метро
            Шаги:
                1. Приблизить карту минимум 4 раза
                2. Кликнуть по любым координатам Оперного театра
                3. Кликнуть по найденной ближайшей станции метро
            Ожидаемый результат:
                Появится карточка метро с соответствующим названием
        """
        self.page.scale_bar.increase(4)
        self.page.map.click('Оперный театр')
        self.page.geo_card.near_stop()

        self.assertEqual(self.page.metro_card.title, "Площадь Ленина")

    def test_click_object_and_gallery(self):
        """
            Test Case:
                Проверка возможности просмотра фотографий организации
            Шаги:
                1. Приблизить карту минимум 4 раза
                2. Кликнуть по любым координатам Оперного театра
                3. Кликнуть по кнопке Фото
            Ожидаемый результат:
                Появится карточка с фотографиями и адресом оррганизации
        """
        self.page.scale_bar.increase(4)
        self.page.map.click('Оперный театр')
        address = self.page.geo_card.address_link
        self.page.geo_card.photos()

        self.assertEqual(address, self.page.gallery_card.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
