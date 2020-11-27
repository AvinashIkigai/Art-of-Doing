print("Welcome to the shipping Accounts Program\n")

#define usernames
users =['eramom','footea','davisv','papinukt','allenj']

username = input("Hello, what is your username: ").lower().strip()

#Are user are in our list...
if username in users:
    # print a price summary
    print("\nHello " + username +". Welcome back to your account.")
    print("Current shipping prices are as follows:")
    print("\nShipping orders 1 to 99: \t\t$5.10 each")
    print("Shipping orders 100 to 499: \t$5.00 each")
    print("Shipping orders 500 to 999: \t$4.95 each")
    print("Shipping orders over 1000: \t\t$4.80 each\n")

    #Determine price based on how many items are shipped
    quantity = int(input("How many item would you like to ship: "))
    if quantity <= 0:
        print("Invalid input")
    elif quantity > 0 and quantity < 100:
        cost = 5.10
    elif quantity >= 100 and quantity < 499:
        cost = 5.00
    elif quantity >= 500 and quantity < 999:
        cost = 4.95
    else:
        cost = 4.80



    #Display final cost
    bill = quantity * cost
    bill = round(bill, 2)
    print("To ship " + str(quantity) + " items, it will cost you $" + str(bill) + " at " + str(cost) + " per item")

    # Place the order
    choice = input("\nWould you like to place this order (y/n): ").lower()
    if choice.startswith('y'):
        print("Okay. Shipping your " + str(quantity) + " items.")
    else:
        print("Okay, no ordr is being placed at this time.")

#Our user is not in the list
else:
    print("Sorry, you don't have account with us. Goodbye..")