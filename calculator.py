import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

print("Scientific Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Sin")
print("8. Cos")

choice = input("Enter choice: ")

if choice in ['1','2','3','4','5']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(subtract(num1, num2))
elif choice == '3':
    print(multiply(num1, num2))
elif choice == '4':
    print(divide(num1, num2))
elif choice == '5':
    print(power(num1, num2))
elif choice == '6':
    num = float(input("Enter number: "))
    print(square_root(num))
elif choice == '7':
    num = float(input("Enter number (radians): "))
    print(sin(num))
elif choice == '8':
    num = float(input("Enter number (radians): "))
    print(cos(num))
else:
    print("Invalid input")
    