#Calculator App

def add(a,b):
    """Add two numbers and return"""
    summation = round(a+b,4)
    print("The sum of " +str(a) + " and " + str(b) + " is " +str(summation))
    return str(a) + " + " + str(b) + " = " + str(summation)


def subtract(a,b):
    """Subtract two numbers and return"""
    difference = round(a-b,4)
    print("The difference of " +str(a) + " and " + str(b) + " is " +str(difference))
    return str(a) + " - " + str(b) + " = " + str(difference)


def multiply(a,b):
    """Multiply two numbers and return"""
    product = round(a*b,4)
    print("The product of " +str(a) + " and " + str(b) + " is " +str(product))
    return str(a) + " * " + str(b) + " = " + str(product)


def divide(a,b):
    """Divide two numbers and return"""
    if b != 0:
        quotient = round(a/b,4)
        print("The quotient of " + str(a) + " and " + str(b) + " is " + str(quotient))
        return str(a) + " / " + str(b) + " = " + str(quotient)
    else:
        print("You can not divide by zero.")
        return "DIV ERROR"


def exponent(a,b):
    """Take a number to a power and return"""
    power = round(a**b,4)
    print("The result of " +str(a) + " raised to the " + str(b) + " power is " +str(power))
    return str(a) + " ^ " + str(b) + " = " + str(power)


#The main code
print("Welcome to the Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed.")

history = []
running = True

while running:
    #Get user input
    num1 = float(input("\nEnter a number: "))
    num2 = float(input("Enter a number: "))
    operator = input("Enter an operation (addition,subtraction,division,exponentiation): ").lower()

    if operator == 'addition' or operator == 'a':
        result = add(num1,num2)
    elif operator == 'subtraction' or operator == 's':
        result = subtract(num1,num2)
    elif operator == 'multiplication' or operator == 'm':
        result = multiply(num1,num2)
    elif operator == 'division' or operator == 'd':
        result = divide(num1,num2)
    elif operator == 'exponentiation' or operator == 'e':
        result = exponent(num1,num2)
    else:
        print("That is not a valid operation. Try again.")
        result = "OPP ERROR"
    history.append(result)

    choice = input("Would you like to run program again (y/n): ").lower()
    if choice != 'y':
        print("\nCalculation Summary: ")
        for calc in history:
            print(calc)
        print("\nThank you for using the Python Calculator App. Goodbye.")
        running = False