import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from training214.day214 import run_of_the_day_214
from training224.day224 import run_of_the_inheritance
from training224.day224 import run_of_the_polymorphism
from training234.miniprjwithpandas import filter_data
from training234.day234 import run_of_the_day234

def main():
    while True:
        print("Choose an action  ")
        print("1. Check  training day 21/4.")
        print("2. Check training day 22/4.")
        print("3. Check training day 23/4.")
        print("4. Check exercise  .")
        print("5. Exit")
        choice = input("Choose ur number: \n")
        if choice == '1':
            run_of_the_day_214()
        elif choice == '2':
            while True :
                print("1. Check  eg Inhertance  .")
                print("2. Check  eg Polymorphism .")
                choice_of_day= input("Choose ur number: \n")
                if choice_of_day == '1':
                   run_of_the_inheritance()
                elif choice_of_day == '2':
                   run_of_the_polymorphism()
        elif choice == '3':
            run_of_the_day234()
        elif choice == '4':
            filter_data()
        elif choice == '5':
            break

main()
