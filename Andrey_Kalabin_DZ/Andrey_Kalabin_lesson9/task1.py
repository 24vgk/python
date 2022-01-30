import time


class TrafficLight:
    __color = 'Красный'

    def running(self, r=4, y=2, g=3) -> None:
        """
        перебирает цвета светофора с определенной задержкой
        :param r:
        :param y:
        :param g:
        :return:
        """
        sleep1 = r
        print(f"{self.__color} {r} сек")
        while sleep1:
            time.sleep(1)
            sleep1 -= 1
        color2 = TrafficLight
        color2.__color = 'Желтый'
        sleep2 = y
        print(f"{self.__color} {y} сек")
        while sleep2:
            time.sleep(1)
            sleep2 -= 1
        color3 = TrafficLight
        color3.__color = 'Зеленый'
        sleep3 = g
        print(f"{self.__color} {g} сек")
        while sleep3:
            time.sleep(1)
            sleep3 -= 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()