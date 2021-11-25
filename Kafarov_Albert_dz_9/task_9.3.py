

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname}, {self.position}'
        print(full_name)

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Совокупный доход ${total_income}')


pixies = Position('Блэк', 'Фрэнсис', 'фронтмен группы Pixies', 10000, 5000)
led_zeppelin = Position(
    'Джимми', 'Пейдж', 'гитарист группы Led Zeppelin', 12000, 7000)
pixies.get_full_name()
pixies.get_total_income()
led_zeppelin.get_full_name()
led_zeppelin.get_total_income()
