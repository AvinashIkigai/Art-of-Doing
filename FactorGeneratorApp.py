print("Welcome to the Factor Generator App")

running = True
while running:
    number = int(input("\nEnter a number to determine all factors of that number: "))
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
            print(i)

    print("\nFactors of " + str(number) + " are: ")
    for factor in factors:
        print(factor)

    print("\nIn summary: ")
    for i in range(int(len(factors)/2)):
        print(str(factors[i]) + " * " + str(factors[-i-1]))

    choice = input("\nRun again(y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for using the program. Have a great day.")