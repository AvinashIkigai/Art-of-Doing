print("Welcome to the Even Odd Number Sorter App")

running = True
while running:
    num_string =input("\nEnter in a string of numbers seperated by a comma (,): ")
    num_string = num_string.replace(' ', '')
    num_list = num_string.split(",")

    evens = []
    odds = []

    print("\n----Result Summary----")
    for number in num_list:
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            print("\t" + str(number) + " is even!")
        else:
            odds.append(number)
            print("\t" + str(number) + " is odd!")

    evens.sort()
    odds.sort()

    print("\nThe following " + str(len(evens)) +" numbers are even: ")
    for even in evens:
        print("\t"+str(even))

    print("\nThe following " + str(len(odds)) + " numbers are odd: ")
    for odd in odds:
        print("\t" + str(odd))

    choice =input("\nWould you like to run the program again(y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for using this program. GoodBye!")

