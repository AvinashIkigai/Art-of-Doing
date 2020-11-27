print("Welcome To Average Calculator App")

#User's Input
name = input("What is your name: ").title().strip()
grade_num = int(input("How many grades would you like to enter: "))

grades = []
for i in range(grade_num):
    grades.append(int(input("Enter grade: ")))

#Short the Grades
grades.sort(reverse=True)
print("\nGrades Highest To Lowest:")
for grade in grades:
    print("\t"+str(grade))

#Average Calculation
average = sum(grades)/len(grades)
average = round(average,2)

#Print a grade summary
print("\n" + name + "'s Grade Summary:")
print("\tTotal Number of Grades: " + str(len(grades)))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage : " +str(average))

#Get the user's desired average and calculate what the need to get on the next assignment
desired_avg = float(input("\nWhat is your desired average: "))
grade_req = desired_avg*(len(grades)+1) - sum(grades)
grade_req = round(grade_req,2)

print("\nGood Luck " + name + "!")
print("You will need to get a " + str(grade_req) + " on your next assignment to earn a " + str(desired_avg) +" average")

#Make a copy of the original grade and swap out one of the grades
new_grades = grades[:]
print("\nLets see what you average could have been if you did better/worse on an assignment.")
grade_change = int(input("What grade would you like to change: "))
new_grades.remove(grade_change)

new_grade = int(input("What grade would you like to change " + str(grade_change) + " to: "))
new_grades.append(new_grade)

#Short the new Grades and print
grades.sort(reverse=True)
print("\nGrades Highest To Lowest:")
for grade in new_grades:
    print("\t"+str(grade))


#Average Calculation
new_average = sum(new_grades)/len(new_grades)
new_average = round(new_average,2)

#Print a new grade summary
print("\n" + name + "'s New Grade Summary:")
print("\tTotal Number of Grades: " + str(len(new_grades)))
print("\tHighest Grade: " + str(max(new_grades)))
print("\tLowest Grade: " + str(min(new_grades)))
print("\tAverage : " +str(new_average))

#Print a summary on how the average changed
print("\nYour new average would be a " + str(new_average) +" comapared to your real average of " + str(average) + "!")
average_change = new_average - average
average_change = round(average_change,2)
print("That is a change of " + str(average_change) + " points!")

#Too bad the original grades are still intact
print("\nToo bad the original grades are still the same")
print(grades)
print("You should go ask for extra credit! ")