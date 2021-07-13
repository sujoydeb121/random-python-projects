class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def __sub__(self):
        return self.num1 - self.num2


# num1 = float(input('enter a number: '))
# num2 = float(input('enter another number: '))

# obj = Calculator(num1, num2)

# choice = 1
# while choice != 0:
#     print("1 for addition")
#     print("2 for subtraction")
#     choice = int(input('enter your choice between 1 or 2: '))
#     if choice == 1:
#         print(obj.add())
#         choice = 0
#     elif choice == 2:
#         print(obj.__sub__())
#         choice = 0
#     else:
#         choice = 0
