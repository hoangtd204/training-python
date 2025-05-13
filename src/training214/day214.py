#demo sử dụng class,object,constructor,
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Helu i'm {self.name}.i'm {self.age} yrs old")

    def __del__(self):
        print(f"{self.name} has been removed ")


def run_of_the_day_214():
 student1 = Student("Alice", 20)
 student2 = Student("Bob", 22)
 student1.say_hello()
 student2.say_hello()



