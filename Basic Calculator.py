'''Trying to figure out how to code a calculator which can to do addition,
subtraction, multiplication, division, and exponents.'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def index(x, y):
    return x ** y

num1 = float(input("Enter first number: "))

print("Select operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Index")

while True:
    operation = input("Enter choice: 1, 2, 3, 4, or 5: ")
    if operation in ('1', '2', '3', '4', '5'):
        num2 = float(input("Enter second number: "))
        break
    else:
        print("Invalid entry, please try again")
        

if operation =='1':
    print(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))
    
elif operation =='2':
    print(str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2)))
    
elif operation =='3':
    print(str(num1) + " x " + str(num2) + " = " + str(multiply(num1, num2)))
    
elif operation =='4':
    print(str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2)))
    
elif operation =='5':
    print(str(num1) + " ^ " + str(num2) + " = " + str(index(num1, num2)))
    

