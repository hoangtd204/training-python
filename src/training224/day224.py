
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass


def run_of_the_day_224():
    dog = Dog("Bong")
    dog.eat()
