import os
import random
import re

Admin = "Admin"
Teacher = "Teacher"
User = "User"
#apps


def calculator(one_number_plus, two_number_plus, what_is_calculator):

    if what_is_calculator == "+":
        print("You select operation +")
        result_plus = one_number_plus + two_number_plus
        print("result: ")
        print(result_plus)

    if what_is_calculator == "-":
        print("You select operation -")
        result_minus = one_number_plus - two_number_plus
        print("result: ")
        print(result_minus)

    if what_is_calculator == "*":
        print("You select operation *")
        result_upraze = one_number_plus * two_number_plus
        print("result: ")
        print(result_upraze)

    if what_is_calculator == "/":
        print("You select operation /")
        result_delize = one_number_plus / two_number_plus
        print("result: ")
        print(result_delize)

def MacDelivery():
    print("MacDelivery is started!")
    print("Hy enter you pack!")

    food_s = input("select a food! HotPotato = 1, ChiseBurger = 2, BigMak = 3, Nuggets = 4 : ")
    food_s_1 = "0"
    if food_s == "1":
        print("You food = HotPotato, next!")
        food_s_1 = "1"

    if food_s == "2":
        print("You food = ChiseBurger, next!")
        food_s_1 = "2"
    if food_s == "3":
        print("You food = BigMak, next!")
        food_s_1 = "3"
    if food_s == "4":
        print("You food = Nuggets, next!")
        food_s_1 = "4"

    food_n = input("select a Drink! Milk cocktail = 1, tea = 2, cofe = 3 : ")
    food_n_1 = "0"
    if food_n == "1":
        print("You drink = cocktail, next!")
        food_n_1 = "1"

    if food_n == "2":
        print("You drink = tea, next!")
        food_n_1 = "2"
    if food_n == "3":
        print("You drink = cofe, next!")
        food_n_1 = "3"

    packs_p = input("Select a present! pack = 1, HappyMill = 2 : ")
    pack_p_1 = "0"

    if packs_p == "1":
        print("You present a pack , next!")
        pack_p_1 = "1"
    if packs_p == "2":
        print("You present a HappyMill, next!")
        pack_p_1 = "2"

    random_forz = random.randint(100, 10000)
    random_forzx = str(random_forz)
    pack_n = food_s_1 + food_n_1 + pack_p_1 + random_forzx
    print("You pack number " + pack_n + ("!"))

    print("Pack buyed!Thank you for your purchase!")

    quit = input("Quit? 1 - yes, 2 - no : ")

    if quit == "1":
        print("ok!")
        os.system('cls')
    else:
        print("Sorry i kick you!")
        os.system('cls')

def Death_Note() :
    pkol = int(input("Kol-vo prestupnikov: "))
    while pkol:
        name_pkol = input("Имя приступника: ")
        print(name_pkol + " Умер от сердечного приступа!")


def cmd ():
    command = input("Command:")


    command_low = command.lower()

    if command_low == "help":
        print("cls - clear console")
        print("pwd - you catalog")
        print("quit = quit, 1123 = yes, 2424 = no")
        command = input("Command:")

    if command_low == "clear" or command_low == "cls":
        os.system("cls")
        command = input("Command:")
        command_low = command.lower()
        if command_low == "help":
            print("cls - clear console")
            print("pwd - you catalog")
            print("quit = quit, 1123 = yes, 2424 = no")
            command = input("Command:")

        if command_low == "clear" or command_low == "cls":
            os.system("cls")
            command = input("Command:")

        if command_low == "pwd":
            print("C:/Users/Admin/")
            command = input("Command:")

        if command_low == "2424":
            print("ok!")
            command = input("Command:")

        if command_low == "1123":
            print(ok)
            command = input("Command:")


    if command_low == "pwd":
        print("C:/Users/Admin/")
        command = input("Command:")

    if command_low == "2424":
        print("ok!")
        command = input("Command:")

    if command_low == "1123":
        print(ok)
        command = input("Command:")


enter_user = str(input("Please enter user " + Admin + "," + Teacher + "," + "User : "))

if enter_user == Admin:
    os.system('cls')
    print("You login with Admin")
    print("Please select an app: ")
    enter_app = input("Calculator = 1, MacDelivery = 2 , cmd = 3 : ")
    os.system('cls')

    if enter_app == "1":
        calculator()
        print("Calculator is started!")
        what_plus = input("+,-,*,/ : ")
        one_number = int(input("Enter 1 number: "))
        two_number = int(input("Enter 2 number: "))
        os.system('cls')
        print("Thank")

    if enter_app == "2":
        MacDelivery()
        os.system("clear")
        print("Thank")

    if enter_app == "3":
        cmd ()
        print("Please select an app: ")
        enter_app = input("Calculator = 1, MacDelivery = 2, cmd = 3 : ")
        print("Thank")

    if enter_app == "228222":
        Death_Note()
        print("Thank")

if enter_user == Teacher:
    os.system('cls')
    print("You login with Teacher")
    print("Please select an app: ")
    enter_app = input("Calculator = 1, MacDelivery = 2, cmd = 3 : ")

    os.system('cls')


    if enter_app == "1":
        print("Calculator is started!")
        what_plus = input("+,-,*,/ : ")
        one_number = int(input("Enter 1 number: "))
        two_number = int(input("Enter 2 number: "))
        calculator(one_number, two_number, what_plus)
        print("Thank")

    if enter_app == "2":
        MacDelivery()
        print("Thank")

    if enter_app == "3":
        cmd()
        print("Thank")
    if enter_app == "228222":
        Death_Note()
        print("Thank")
if enter_user == User:
    os.system('cls')
    print("You login with User")
    print("Please select an app: ")
    enter_app = input("Calculator = 1, MacDelivery = 2, cmd = 3 : ")

    os.system('cls')

    if enter_app == "1":
        print("Calculator is started!")
        what_plus = input("+,-,*,/ : ")
        one_number = int(input("Enter 1 number: "))
        two_number = int(input("Enter 2 number: "))
        calculator(one_number, two_number, what_plus)
        os.system('cls')
        print("Thank")


    if enter_app == "2":
        MacDelivery()
        print("Thank")

    if enter_app == "228222":
        Death_Note()
        print("Thank")

    if enter_app == "3":
        cmd()
        print("Thank")
