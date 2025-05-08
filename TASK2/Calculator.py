import math
import datetime
now = datetime.datetime.now()
print("************************************CALCULATOR****************************************")
print("                                                         ######____Created by HARSHITA RAI____######")
print("                                                         ####__Created on May 05,2024 --- 17:00 PM__####")
print(f"                                                        ##########___Current date is:-{now}___##########")
user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:
                  Enter -1 to exit \nEnter you answer here:-'''))

while True:
    if user_input == -1:
        break
    else:      
        if user_input == 1:
            print("-----You Choosed Addition------")
            i = 0
            SUM = 0
            while i != -1:
                i = -int(input("Enter a number:"))
                if i == -1:
                    break
                else:
                    SUM = SUM + i
                    i = i+1
            print("The sum of numbers is:-", SUM)
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 2:
            print("------You choosed Substraction-----")
            c = int(input("Enter first number:"))
            d = int(input("Enter second number:"))
            D = c-d
            print("The difference of two numbers is:",D)
            user_input = int(input('''  
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 3:
            print("-----You choosed Multiplication-----")
            e = int(input("Enter first number:"))
            f = int(input("Enter second number:"))
            M = e*f
            print("The multiplication is:", M)
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 4:
            print("-----You choosed Division-----\n")
            g = int(input("Enter first number:"))
            h = int(input("Enter second number:"))
            Div = g*h
            print("The answer is:", Div)
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 5:
            print("-----You choosed Percenage-----\n")
            num1 = int(input("How many percent you want to calculate:"))
            num2 = int(input("Enter number of which you want to calculate percentage:"))
            v1 = float(num1 / 100)
            v2 = float(v1 * num2)
            print("The percentage of given number is:", v2)
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 6:
            print("-----You choosed for Sin value calculation-----\n")
            num = int(input("Enter a number:"))
            print(f"The Sin value of {num} is:-", math.sin(num))
            ad = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 7:
            print("-----You choosed for Cos value calculation-----\n")
            num = int(input('Enter a number:-'))
            print(f"The cos value of {num} is:", math.cos(num))
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 8:
            print("-----You choosed for Tan value calculation-----\n")
            num = int(input('Enter a number:-'))
            print(f"The tan value of {num} is:", math.tan(num))
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 9:
            print("-----You choosed Square root calculation-----\n")
            num = int(input('Enter a number:-'))
            print(f"The Square root of {num} is:", math.sqrt(num))
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 10:
            print("-----You choosed Power calculation-----\n")
            num1 = int(input('Enter a number:-'))
            num2 = int(input("How many power  you want to calculate:-"))
            print(f"The power  of {num1} is:", math.pow(num1, num2))
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 11:
            print("-----You choosed for factorial calculation-----\n")
            num = int(input('Enter number of which you want to calculate factorial:-'))
            print(f"The Factorial of {num} is:", math.factorial(num))
            user_input = int(input('''
                  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 12:
            num = int(input('Enter a number:-'))
            print(f"The Log value of {num} is:", math.log10(num))
            user_input = int(input('''\t\t\t\t  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))

        elif user_input == 13:
            num = int(input('Enter a number:-'))
            print(f"The Exponent value of {num} is:", math.exp(num))
            user_input = int(input('''\t\t\t\t  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))
        else:
            print("********** INVALID INPUT **********")
            user_input = int(input('''\t\t\t\t  Enter 1 for addition:
                  Enter 2 for subtraction:
                  Enter 3 for multiplication:
                  Enter 4 for division:
                  Enter 5 for calculating percentage:
                  Enter 6 for calculating Sin value:
                  Enter 7 for calculating Cos value:
                  Enter 8 for calculating Tan value:
                  Enter 9 for calculating Square root:
                  Enter 10 for calculating Power:
                  Enter 11 for calculating Factorial:
                  Enter 12 for calculating Log:
                  Enter 13 for calculating Exponent:\nEnter you answer here:-'''))




