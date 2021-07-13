from calculator import *
import sys
sys.path.append('.')

# choose user input
num1 = float(input('enter a number: '))
num2 = float(input('enter another number: '))

obj = Calculator(num1, num2)

# choose your operation
choice = 1
while choice != 0:
    print("1 for addition")
    print("2 for subtraction")
    choice = int(input('enter your choice between 1 or 2: '))
    if choice == 1:
        print(obj.add())
        choice = 0
    elif choice == 2:
        print(obj.__sub__())
        choice = 0
    else:
        print('wrong input from the user')
        choice = 0
