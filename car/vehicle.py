class Vehicle:
    type = None
    engine = None

    def __init__(self, type, engine):
        self.type = type
        self.engine = engine

    def details(self):
        print(f"{self.type} and {self.engine}")

    def start(self):
        print(f"Starting {self.type}")


# class DeepikasImplementation(MyMLLibraryClass):
#     def train(self):
class MotorBike(Vehicle):
    name = None

    def __init__(self, name, engine):
        Vehicle.__init__(self, "motorbike", engine)
        self.name = name

    def start(self):
        print("Vrrom Vroom")



class Car(Vehicle):
    def __init__(self, engine):
        Vehicle.__init__(self, "car", engine)

