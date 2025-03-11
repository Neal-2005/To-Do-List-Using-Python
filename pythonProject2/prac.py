class Car:
    max_speed = 120

    def __init__(self, make, model, color, opSpeed = 0):
        self.make = make
        self.model = model
        self.color = color
        self.opSpeed = opSpeed
        self.opSpeed =  20

    def accelerate(self, acceleration):
        if self.opSpeed + acceleration <= Car.max_speed:
            self.opSpeed += acceleration
        else:
            self.opSpeed = Car.max_speed

    def get_Speed(self):
        return self.opSpeed

a = 1
def do(x):
    a = 100
    return x + a


print(do(1))


car1 = Car("Toyota", "Camry", "Blue", 90)
car2 = Car("Honda", "Civic", "Red", 90)

car1.accelerate(30)
car2.accelerate(20)

print(f"{car1.make} {car1.model} is currently at {car1.get_Speed()} km/h")
print(f"{car2.make} {car2.model} is currently at {car2.get_Speed()} km/h")

car1.opSpeed = 20
print(car1.opSpeed)


