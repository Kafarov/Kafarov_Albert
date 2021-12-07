

def get_store_name(store):
    if store == moscow_store:
        return 'Московский склад'
    elif store == spb_store:
        return 'склад в СПб'
    else:
        return 'склад в Екб'


moscow_store = {}
spb_store = {}
ekb_store = {}


class Warehous:

    def app(self, store):
        if self.name in store:
            store[self.name] += self.amount
            print(
                f'Объект {self.name} в количестве {self.amount} шт отправлен на {get_store_name(store)}')
        else:
            store[self.name] = self.amount
            print(
                f'Объект {self.name} в количестве {self.amount} шт отправлен на {get_store_name(store)}')

    @classmethod
    def popit(cls, name, amount, store):  # :)
        if name in store:
            if store.get(name) > amount:
                store[name] -= amount
                print(
                    f'Объект {name} в количестве {amount}шт отгружен из {get_store_name(store)}')
            else:
                print(
                    f'На {get_store_name(store)} не достаточно {name} для отгрузки в количестве {amount}шт')
        else:
            print(f'Объект отсутсвует на {get_store_name(store)}')

    @classmethod
    def str(cls, store, name):
        if name in store:
            print(
                f'На {get_store_name(store)} обект {name} в количестве {store.get(name)}')
        else:
            return f'{name} отсутствует на {get_store_name(store)}'


class OffiseEqip(Warehous):

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Printer(OffiseEqip):

    def __new__(cls, name, amount):
        try:
            if int(amount):
                if amount > 0:
                    print(f'Создан объект {name}')
                    return super().__new__(cls)
                else:
                    print('Задано неверное количество принтеров')

        except ValueError:
            print('Задано неверное количество принтеров')


class Scanner(OffiseEqip):

    def __new__(cls, name, amount):
        try:
            if int(amount):
                if amount > 0:
                    print(f'Создан объект {name}')
                    return super().__new__(cls)
                else:
                    print('Задано неверное количество сканеров')

        except ValueError:
            print('Задано неверное количество сканеров')


class CopyMachine(OffiseEqip):

    def __new__(cls, name, amount):
        try:
            if int(amount):
                if amount > 0:
                    print(f'Создан объект {name}')
                    return super().__new__(cls)
                else:
                    print('Задано неверное количество копировальных аппаратов')

        except ValueError:
            print('Задано неверное количество копировальных аппаратов')


equipment_1 = Printer('Xerox Phaser 3020', 6)
equipment_2 = Printer('Xerox Phaser 3020', 3)
equipment_3 = Scanner('Canon Canoscan LIDE300', 5)
equipment_4 = CopyMachine('HP LaserJet Pro MFP M28a', 10)

equipment_1.app(moscow_store)
equipment_2.app(moscow_store)
equipment_3.app(spb_store)
equipment_4.app(ekb_store)
Warehous.popit('Xerox Phaser 3020', 2, moscow_store)
