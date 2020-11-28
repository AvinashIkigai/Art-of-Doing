print("Welcome to the Voter Registration App\n")

name = input("\nPlease enter your name: ").title().strip()
age = int(input("Please enter your age: "))

parties = ['Republican','Democratic','Independent','Libertarian','Green']
if age > 0 and age < 18:
    print("Hello, "+name+" you are not eligible to vote! ")
else:
    print("Congratulation,"+name+" You are eligible to register for vote ")
    print("Here is a list of political parties to join:")

    #Display Political Parties
    for partie in parties:
        print("\t- "+partie)
    choice = input("\nWhat party would you like to join: ").title().strip()
    if choice in parties:
        print("\nCongratulation " + name +"! you have joined the " + choice + " party!")
        if choice == "Republican" or choice == "Democratic":
            print("That is a major party!")
        elif choice == 'Independent':
            print("You are a independent person!")
        else:
            print("That is not a major party.")
    else:
        print("That is not a given party.")

