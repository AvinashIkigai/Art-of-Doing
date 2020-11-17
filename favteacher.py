print("Welcome to the Favorite Teachers Program\n")
fav_teachers = []

# Get user input
fav_teachers.append(input("Who is your first favorite teacher: ").title())
fav_teachers.append(input("Who is your second favorite teacher: ").title())
fav_teachers.append(input("Who is your third favorite teacher: ").title())
fav_teachers.append(input("Who is your fourth favorite teacher: ").title())

# Summery of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your Favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your Favorite teachers in reverse alphabetical order are: " +
      str(sorted(fav_teachers, reverse=True)))

print("\nYour top two teachers are " +
      fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are " +
      fav_teachers[2] + " and " + fav_teachers[3])
print("Your last favorite teacher is " + fav_teachers[-1] + " .")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

# Insert a new favorite teacher
fav_teachers.insert(0, input(
    "\nOpps, " + fav_teachers[0] + " is no longer favorite teacher. Who is your new favorite teacher: ").title())

# Summery of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your Favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your Favorite teachers in reverse alphabetical order are: " +
      str(sorted(fav_teachers, reverse=True)))
print("\nYour top two teachers are " +
      fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are " +
      fav_teachers[2] + " and " + fav_teachers[3])
print("Your last favorite teacher is " + fav_teachers[-1] + " .")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

# Remove a teacher
fav_teachers.remove(input(
    "\nYou have decided you no longer like a teacher, which teacher would you like to remove from the list:").title())
# Summery of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your Favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your Favorite teachers in reverse alphabetical order are: " +
      str(sorted(fav_teachers, reverse=True)))
print("\nYour top two teachers are " +
      fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are " +
      fav_teachers[2] + " and " + fav_teachers[3])
print("Your last favorite teacher is " + fav_teachers[-1] + " .")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")
