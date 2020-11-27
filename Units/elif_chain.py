#Elif Chains

age = int(input("What is your age: "))

if age <= 0:
    print("Invalid Entry")
elif age < 18:
    print("you're only " + str(age) + " !")
    print("You can not gamble! ")
elif age >=18 and age < 21:
    print("OKay, so you are " + str(age) + "! ")
    print("You can play BlackJack but you can't have a drink")
else:
    print("OKay good. You are " + str(age) + "!")
    print("You can play BlackJack and also can have a drink")