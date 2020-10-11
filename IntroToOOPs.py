from car.vehicle import Car, MotorBike


if __name__ == "__main__":
    bmw = Car(2500)
    bmw.details()

    kawasaki = MotorBike("kawasaki", 500)
    kawasaki.details()

    bmw.start()
    kawasaki.start()

