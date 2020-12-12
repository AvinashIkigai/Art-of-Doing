import time
print("Welcome to the Prime Number App")

running = True
while running:
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime number within a set range.")

    option = input("Enter your choice 1 or 2: ")
    if option == '1':
        number = int(input("\nEnter a number to determine if it is prime or not: "))
        prime_status = True
        for i in range(2, number):
            if number % i == 0:
                prime_status = False
                break
        if prime_status:
            print(str(number) + " is prime")
        else:
            print(str(number) + ' is not prime')
    elif option == '2':
        l_bound = int(input("\nEnter the lower bound of your range: "))
        u_bound = int(input("\nEnter the upper bound of your range: "))

        primes = []
        start_time = time.time()

        for prime_candidate in range(l_bound, u_bound + 1):
            if prime_candidate > 1:
                prime_status = True
                for i in range(2, prime_candidate):
                    if prime_candidate % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False

            if prime_status:
                primes.append(prime_candidate)

        end_time = time.time()
        delta_time = round(end_time - start_time, 4)
        print("Calculation took a total of " + str(delta_time) + " seconds.")
        print("\nThe following number between " + str(l_bound) + " and " + str(u_bound) + " are prime: ")
        input("Press enter to continue")

        for prime in primes:
            print(prime)
    else:
        print("\nThat is not a valid options.")

    choice = input("Would you like to run the program again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("\nThank you for using the program. Have a nice day")