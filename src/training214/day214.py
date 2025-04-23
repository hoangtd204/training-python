#demo sử dụng class,object,constructor,
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHello(self):
        print(f"Helu i'm{self.name}.i'm {self.age} yrs old")

    def __del__(self):
        print(f"{self.name} has been removed ")

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

student1.sayHello()
student2.sayHello()

