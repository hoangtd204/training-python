
class Animal:
    def speak(self):
        print("Animal is speaking \n")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog is barking")

def run_of_the_day234():
    animal = Animal()
    dog = Dog()

    animal.speak()
    dog.speak()

