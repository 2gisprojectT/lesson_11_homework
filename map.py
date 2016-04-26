from base_component import BaseComponent


class Map(BaseComponent):
    selectors = {
        'self': '.map',
    }

    __place_coordinates_with_zoom = {
        'Центральный округ': {1: [950, 300]},
        'Первомайский сквер': {4: [1100, 270]},
        'Оперный театр': {4: [1250, 210]}
    }

    scale = 1

    def click(self, place):
        self.actions.move_to_element_with_offset(self.element,
                                                 self.__place_coordinates_with_zoom[place][self.scale][0],
                                                 self.__place_coordinates_with_zoom[place][self.scale][1])\
            .click().perform()
