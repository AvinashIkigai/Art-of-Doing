print("Welcome to the Basketball Roster Program")

#Get user input and define our roster
roster = []
player = input("\nWho is your point gaurd: ").title()
roster.append(player)
player = input("Who is your shooting gaurd: ").title()
roster.append(player)
player = input("Who is your small forward: ").title()
roster.append(player)
player = input("Who is your power forward: ").title()
roster.append(player)
player = input("Who is your center: ").title()
roster.append(player)

#Display Roster
print("\n\tYour starting 5 for the upcoming basketball season\n")
print("\t\tPoint Gaurd:\t\t " +roster[0])
print("\t\tShooting Gaurd:\t\t " +roster[1])
print("\t\tSmall Forward:\t\t " +roster[2])
print("\t\tPower Forward:\t\t " +roster[3])
print("\t\tCenter:\t\t\t" +roster[4])

#Remove an injured player
injure_player = roster.pop(2)
print("\nOh no, " + injure_player + " is injured.")
roster_length = len(roster)
print("Your roster only has " + str(roster_length) + " player.")

#Add a new player
added_player = input("Who will take "+ injure_player + "'s spot: ").title()
roster.insert(2,added_player)

#Display Roster
print("\n\tYour starting 5 for the upcoming basketball season\n")
print("\t\tPoint Gaurd:\t\t " +roster[0])
print("\t\tShooting Gaurd:\t\t " +roster[1])
print("\t\tSmall Forward:\t\t " +roster[2])
print("\t\tPower Forward:\t\t " +roster[3])
print("\t\tCenter:\t\t\t" +roster[4])

print("\nGood luck "+ roster[2] + " you will do great!")
roster_length = len(roster)
print("Your roster now has " +str(roster_length)+ " players.5")
