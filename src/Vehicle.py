class Vehicle:
    def __init__(self, model_name, engine_power, color, manufacture_year, manufacture_country, doors_сount, hijacked_status):
        self.__model_name = model_name
        self.__engine_power = engine_power
        self.__color = color
        self.__manufacture_year = manufacture_year
        self.__manufacture_country = manufacture_country
        self.__doors_count = doors_сount
        self.__hijacked_status = hijacked_status
        self.__engine_status = False
        self.__headlights_status = False

    @property
    def model_name(self):
        return self.__model_name

    @property
    def engine_power(self):
        return self.__engine_power

    @property
    def color(self):
        return self.__color

    @property
    def manufacture_year(self):
        return self.__manufacture_year

    @property
    def manufacture_country(self):
        return self.__manufacture_country

    @property
    def doors_сount(self):
        return self.__doors_сount

    @property
    def hijacked_status(self):
        if self.__hijacked_status:
            return 'Данное т/с в угоне!'
        else:
            return 'Данное т/с не имеет криминальной истории'

    @property
    def engine_status(self):
        if self.__engine_status:
            return 'Двигатель запущен'
        else:
            return 'Автомобиль не заведен'

    @property
    def headlights_status(self):
        if self.__headlights_status:
            return 'Фары включены'
        else:
            return 'Фары отключены'

    def start_engine(self):
        print('Двигатель запущен')
        self.__engine_status = True

    def stop_engine(self):
        print('Двигатель остановлен')
        self.__engine_status = False

    def switch_on_headlights(self, light_type):
        if light_type == 'ближний':
            print('Включен ближний свет')
            self.__headlights_status = True
        elif light_type == 'дальний':
            print('Включен дальний свет')
            self.__headlights_status = True
        else:
            print('Вы выбрали неверный режим освещения')

    def switch_off_headlights(self):
        print('Фары отключены')
        self.__headlights_status = False


