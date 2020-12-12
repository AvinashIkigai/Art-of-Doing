import random

print("------------------------------Power-Ball Simulator------------------------------")

#Determine the size of the lottery
white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (normally 69): "))
if white_balls < 5:
    white_balls = 5

red_balls = int(input("How many red-balls to draw from for the Power-Ball (normally 26): "))
if red_balls < 1:
    red_balls = 1
#Calculate the odds of winning this specific lottery
odds = 1
for i in range(5):
    odds *= white_balls - i

odds *= red_balls / 120
print(odds)

print("You have a 1 in " + str(odds) + " chance of winning this lottery.")

#Get ticket interval
ticket_interval = int(input("Purchased tickets in what interval: "))

#Generate the winning lottery numbers
#Get the white-ball for ticket
winning_numbers = []
while len(winning_numbers) < 5:
    number = random.randint(1,white_balls)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()

#Get the red-ball for the ticket
number = random.randint(1,red_balls)
winning_numbers.append(number)

#Simulate the powerball drawing
print("----------Welcome to the Power-Ball----------")
print("\nTonight's winning numbers are: ",end="")
for number in winning_numbers:
    print(str(number),end=' ')

input("\nPress 'Enter' to begin purchasing tickets!!!")

ticket_purchased = 0
active = True
tickets_sold = []

while winning_numbers not in tickets_sold and active == True:
    # Make a new lottery ticket for the user to buy
    lottery_number = []
    while len(lottery_number) < 5:
        number = random.randint(1,white_balls)
        if number not in lottery_number:
            lottery_number.append(number)
    lottery_number.sort()

    number = random.randint(1,red_balls)
    lottery_number.append(number)

    if lottery_number not in tickets_sold:
        ticket_purchased += 1
        tickets_sold.append(lottery_number)
        print(lottery_number)

    else:
        print("Losing ticket generated; disregard...")

    #Check if the user want to continue buying tickets
    if ticket_purchased % ticket_interval == 0:
        print(str(ticket_purchased)+" tickets purchased so far with no winners...")
        choice = input("\nKeep purchasing tickets (y/n): ").lower()
        if choice != 'y':
            active = False

#The lottery is now over
if lottery_number == winning_numbers:
    print("\nWinnig ticket numbers: ",end='')
    for number in lottery_number:
        print(str(number), end=' ')
    print("\nPurchased a total of " + str(ticket_purchased) + " tickets.")
else:
    print("\nYou bought " + str(ticket_purchased) + " tickets and still lost!")
    print("Better luck next time!")














