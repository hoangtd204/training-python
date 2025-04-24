import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from training214.day214 import run_of_the_day_214
from training224.day224 import run_of_the_day_224


def main():


    while True:
        print("Chọn hành động thực hiện")
        print("1. Kiểm training day 21/4.")
        print("2. Kiểm training day 22/4.")
        print("3. Thoát")

        choice = input("Chọn: ")
        if choice == '1':
            run_of_the_day_214()
        elif choice == '2':
            run_of_the_day_224()
        elif choice == '3':
            break

main()
