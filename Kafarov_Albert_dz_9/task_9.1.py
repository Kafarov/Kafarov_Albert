from time import sleep


class TrafficLight:

    def __init__(self, __color=['Красный', 'Жёлтый', 'Зеленый']):
        self.__color = __color

    def running(self):
        print('Ctrl+c для выхода')
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(4)
            # print(self.__color[1]) # раскоментировать чтоб светофор работал правлильно
            # sleep(2)


start = TrafficLight()
start.running()
