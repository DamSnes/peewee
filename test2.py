class Point:

    # Конструктор выполняется после создание экземпляра класса с заранее заданными параметрами
    # Методы как простые функции
    # Self имя для ссылки на объект, в контексте которого вызывается метод.
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False


    def getCoordX(self):
        return self.x


    def setCoordX(self, x):
        if Point.checkValue(x):
            self.x = x
        else:
            raise ValueError("Неверный формат данных")


    def delCoordX(self):
        print("Удаление свойства")
        del self.x


    coordX = property(getCoordX, setCoordX, delCoordX)


pt = Point(5, 6)
pt.coordX = 100 # Запись значения
x = pt.coordX # Чтение записи
print(x)
print(Point.__dict__)
del pt.coordX


