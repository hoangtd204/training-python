from training55.demo_request import requestAPI
from trainingday284.day284 import filter_data_miniprj
from training234.day234 import run_of_the_day234
from training234.miniprjwithpandas import filter_data
from training224.day224 import run_of_the_polymorphism
from training224.day224 import run_of_the_inheritance
from training214.day214 import run_of_the_day_214
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


def main():
    while True:
        print("Choose an action  ")
        print("1. Check  training day 21/4.")
        print("2. Check training day 22/4.")
        print("3. Check training day 23/4.")
        print("4. Check training day 22/4.")
        print("5. Check training day 28/4.")
        print("6. Check training day 5/5.")
        print("7 . Exit")
        choice = input("Choose ur number: \n")
        if choice == '1':
            run_of_the_day_214()
        elif choice == '2':
            while True:
                print("1. Check  eg Inhertance  .")
                print("2. Check  eg Polymorphism .")
                choice_of_day = input("Choose ur number: \n")
                if choice_of_day == '1':
                    run_of_the_inheritance()
                elif choice_of_day == '2':
                    run_of_the_polymorphism()
        elif choice == '3':
            run_of_the_day234()
        elif choice == '4':
            filter_data()
        elif choice == '5':
            filter_data_miniprj()
        elif choice == '6':
            requestAPI
        elif choice == '7':
            break
        else:
            print("Wrong choice")


main()
