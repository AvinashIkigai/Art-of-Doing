from collections import Counter
print("Welcome to the Frequency Analysis App")

#List of elements to remove from all text for analysis
non_letters = ['1','2','3','4','5','6','7','8','9','0',' ','.',',','!','?',',','"',"'",':',";",'(',')','%','&','#','$','\n','\t']

#Information for the first key phrase 1
key_phrase_1 = input("\nEnter a word or phrase to count the occurance of each letter: ").lower().strip()

#Removing all non letter from key_phrases_1
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter,'')

total_occurances = len(key_phrase_1)

#Create a counter object
letter_count = Counter(key_phrase_1)

#Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurance\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurances
    percentage = round(percentage,2)
    print("\t"+ key+"\t\t\t"+str(value)+"\t\t\t"+str(percentage)+" %")

#Make a list of letter from highest occurance to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

#Print that list
print("\nLetters ordered from highest occurance to lowest: ")
for letter in key_phrase_1_ordered_letters:
    print(letter,end='')

# Information for the first key phrase 2
key_phrase_2 = input("\n\nEnter a word or phrase to count the occurance of each letter: ").lower().strip()

# Removing all non letter from key_phrases_2
for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurances = len(key_phrase_2)

# Create a counter object
letter_count = Counter(key_phrase_2)

# Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 2: ")
print("\n\tLetter\t\tOccurance\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100 * value / total_occurances
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t\t" + str(value) + "\t\t\t" + str(percentage) + " %")

# Make a list of letter from highest occurance to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_2_ordered_letters.append(pair[0])

# Print that list
print("\nLetters ordered from highest occurance to lowest: ")
for letter in key_phrase_2_ordered_letters:
    print(letter, end='')
