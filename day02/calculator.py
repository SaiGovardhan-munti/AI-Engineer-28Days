

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    

#calculator program
a = float(input("Enter the num1:"))

#choose the ope

operation = input("Enter the opertion:(+,-,*,/)")

b = float(input("Enter the num2:"))


if operation == "+":
    result = add(a,b)
elif operation == "-":
    result = subtract(a,b)   
elif operation == "*":
    result = multiply(a,b)
elif operation == "/":
    result = division(a,b)
else:
    print("Invalid operation")
    result = None

if result is not None:
    print(f"Result: {result}")
