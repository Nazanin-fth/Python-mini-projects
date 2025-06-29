# This program performs basic arithmetic operations based on user input.
x = int(input("Enter a number: \n"))
y = int(input("Enter another number: \n"))
operation = input("Enter the operation you want to perform: \n")


def Sum(a, b):
    result = x + y
    print(f"The result of {x} + {y} is {result}")
def Subtract(a, b):
    result = x - y
    print(f"The result of {x} - {y} is {result}")
def Multiply(a, b):
    result = x * y
    print(f"The result of {x} * {y} is {result}")
def Divide(a, b):
    result = x / y
    print(f"The result of {x} / {y} is {result}")


if operation == "+":    
    Sum(x, y)
elif operation == "-":
    Subtract(x, y)
elif operation == "*":
    Multiply(x, y)  
elif operation == "/":
    Divide(x, y)
else:
    print("Invalid operation. Please enter +, -, *, or /.")
