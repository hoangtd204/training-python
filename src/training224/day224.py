
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass

def run_of_the_inheritance():
    dog = Dog("Bong")
    dog.eat()


# Ví dụ phần polymorphism
class Person:
    def speak(self):
        print("I am a person.")

class Student(Person):
    def speak(self):
        print("I'm studying for exams.")

class Teacher(Person):
    def speak(self):
        print("I'm teaching students.")

#hàm run tùy vào object khác nhau sẽ chạy các phiên bản hàm speak khác nhau
def  run_of_the_polymorphism ():
     people = [Student(), Teacher(), Person()]
     for person in people:
         person.speak()




