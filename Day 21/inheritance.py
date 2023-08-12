class Car:
    def __init__(self):
        self.tyre = 4

    def printTyres(self):
        print(self.tyre)


class Bmw(Car):
    def __init__(self):
        super().__init__()

    def printTyres(self):
        super().printTyres()
        print("bmw Tyres")

    def identification():
        print("It's a BMW")


bmw = Bmw()
bmw.printTyres()
