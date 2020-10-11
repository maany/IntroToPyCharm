class Car:
    make = "None"
    engine = 0

    def __init__(self, make, engine):
        self.make = make
        self.engine = engine

    def print(self):
        print("Make: {make} and Engine {engine}".format(make=self.make, engine = self.engine))
