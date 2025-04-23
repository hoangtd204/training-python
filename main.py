import quanlisv
import students
import json
import os
import re


def main():
    lb = Sms()

    while True:
        print("\n===== MENU =====")
        print("1. Them sinh vien")
        print("2. Xem tat ca sinh vien")
        print("3. Tim kiem thong tin sinh vien")
        print("4. Cap nhat thong tin sinh vien")
        print("5. Xoa thong tin sinh vien")
        print("6. Thoat!")
        choice = input("Chọn: ")

        if choice == "1":
        # Nhập thông tin sinh vien
        
        # elif choice == "2":

        # elif choice == "3":

        # elif choice == "4":

        # elif choice == "5":

        # elif choice == "6":
        #     print("Thoat!")
        #     break

        else:
            print("Lựa chọn không hợp lệ.")
