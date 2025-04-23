from students import Student
import json
import os
import re

#Validate email
def validEmail(email):
    pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    return re.match(pattern, email)

#Validate Phone Number
def validPhone(phone):
    pattern = r'^0\d{9}$'
    return re.match(pattern, phone)

#Check for duplicate student_id
def check_duplicate_studentid(users, name):
    for person in users:
        if person['name'] == name:
            return False
    return True


# #Check for duplicate email
# def valid_Email_Dupli(users, email):
#     for person in users:
#         if person['email'] == email:
#             return False
#     return True

#Check for duplicate phonenumber
# def valid_Phone_Dupli(users, phone):
#     for person in users:
#         if person['phonenumber'] == phone:
#             return False
#     return True

 
            # age = input("Nhap tuoi sinh vien: ")
            # phonenumber = ("Nhap so dien thoai: ")
            # id = input("Nhap cccd: ")
class Sms:
    def __init__(self, file_path= "students.json"):
        self.file_path = file_path
        self.students = []


    def get_user_input (self):
        # while True:
        #  name = input("Nhap ten sinh vien: ")
        #  if valid_Name_Dupli(name):
        #     break
        #  else:
        #     print("T")

        # while True:
        #  student_id = input("Nhap ma sinh vien: ")
        #  if valid_Name_Dupli(name):
        #     break
        #  else:
        #     print("T")
        name = input("Nhap ten sinh vien: ")
        student_id = input("Nhap ma sinh vien: ")
        age = input("Nhap tuoi sinh vien: ")
        phonenumber = ("Nhap so dien thoai: ")
        id = input("Nhap cccd: ")
        new_student = Student(student_id)

        self.students.append(new_student)

