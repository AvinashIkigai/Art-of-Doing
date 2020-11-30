from collections import Counter

print("Welcome to the Code Breaker App")

# List of elements to remove from all text for analysis
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', ',', '!', '?', ',', '"', "'", ':', ";", '(',
               ')', '%', '&', '#', '$','-','_','11', '\n', '\t']

# Information for the first key phrase 1
# key_phrase_1 = input("\nEnter a word or phrase to count the occurance of each letter: ").lower().strip()
key_phrase_1 = '''Lorem ipsum w dolor sit amet, consectetur adipiscing elit. Aenean vulputate mollis justo, non vestibulum erat mollis eget. 
Maecenas iaculis, lectus eu convallis vulputate, massa augue porttitor risus, non vestibulum tortor nisi id libero. Quisque id est tortor. 
Nulla aliquam sem ac metus ultrices consectetur. Vestibulum aliquet et lacus id luctus. In aliquam nisl vitae auctor mattis. Sed mattis ipsum ac pulvinar finibus. 
Donec dui leo, dignissim vitae porttitor molestie, euismod vitae metus. Pellentesque id vulputate libero. 
Sed sollicitudin, turpis ac rhoncus ornare, dolor metus suscipit leo, vel venenatis turpis nisi eu quam. In a ligula urna.
Mauris bibendum consequat porttitor. Nunc eget gravida magna. Cras convallis tincidunt erat, quis tempus diam posuere eu. 
Duis hendrerit eget erat eget vehicula. Vestibulum sed mattis libero. Nulla ante erat, ultrices vehicula facilisis non, facilisis ut nunc. 
Fusce dapibus eu tortor ac accumsan. Quisque porta justo erat, non iaculis ex efficitur sit amet. Praesent pharetra lobortis dapibus. Nulla facilisi. 
In blandit nulla eu malesuada tincidunt. Nunc gravida tincidunt massa sed pretium. Quisque lobortis interdum ex, et finibus tellus gravida at. 
Integer eget lacus sit amet ipsum tincidunt fringilla nec at eros. Fusce erat dolor, scelerisque sed vulputate sit amet, fringilla quis felis. 
Aenean elementum leo non dui bibendum, vel iaculis lorem luctus.Proin ultrices aliquam turpis vitae pellentesque. 
Sed pharetra lobortis sem, et pretium odio ultricies nec. Suspendisse efficitur non massa eget rhoncus. Mauris non condimentum nunc, eu tempus magna. 
Maecenas blandit massa commodo, ultrices eros ac, sagittis arcu. Donec ullamcorper felis eget hendrerit iaculis. In malesuada mauris eget nisi congue facilisis a eu orci. 
Nunc vitae ante dolor. Nullam vel eros vel neque venenatis tempus. Suspendisse id auctor eros. Suspendisse id cursus nibh. Etiam sollicitudin convallis sagittis. 
Praesent quis dictum urna, eget elementum quam. Curabitur ultricies eu diam nec ullamcorper. Morbi nec turpis nec sapien suscipit volutpat.
Nunc lobortis risus ut erat rutrum faucibus. Pellentesque sollicitudin feugiat magna, id cursus massa efficitur quis. Suspendisse potenti. In hac habitasse platea dictumst. 
Ut molestie ut nunc gravida pulvinar. In porttitor purus eleifend nisi laoreet, ac placerat dui cursus. Fusce interdum sollicitudin tortor, eget hendrerit ligula dignissim sed.
Nunc sapien quam, rutrum vitae dictum ac, placerat quis leo. Cras vestibulum nibh lorem, id imperdiet ante blandit iaculis. 
Vestibulum augue velit, sodales quis mollis non, auctor vel purus. In libero nulla, tincidunt quis pulvinar quis, hendrerit ut felis. 
Donec mi diam, finibus sed quam id, fermentum consequat ex. Pellentesque interdum elit in arcu blandit fermentum. Fusce rhoncus augue at efficitur vulputate. 
Cras id orci sit amet metus tincidunt condimentum vitae vel lorem. Cras id purus orci. Proin ornare cursus feugiat. Nullam vel dolor sem. 
Vivamus rhoncus, massa id rutrum sagittis, magna ligula egestas justo, eget ultrices est erat consectetur arcu. Nam malesuada rutrum sapien sit amet aliquet. 
Etiam et laoreet arcu, ac venenatis erat.'''
key_phrase_1 = key_phrase_1.lower()


# Removing all non letter from key_phrases_1
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurances = len(key_phrase_1)

# Create a counter object
letter_count = Counter(key_phrase_1)

# Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurance\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100 * value / total_occurances
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t\t" + str(value) + "\t\t\t" + str(percentage) + " %")

# Make a list of letter from highest occurance to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

# Print that list
print("\nLetters ordered from highest occurance to lowest: ")
for letter in key_phrase_1_ordered_letters:
    print(letter, end='')

# Information for the first key phrase 2
# key_phrase_2 = input("\n\nEnter a word or phrase to count the occurance of each letter: ").lower().strip()

key_phrase_2 = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Protein now, the notebook ugly drink, clinical pot sit Pakistan, 
there is a lot of real estate or alcohol. Various clinical Penatibus Super Bowl mountains instantly. Nam football layer propaganda, but please now. 
Gluten. The latest throat throat computer. Id tellus facilisis posuere, and now were, unable to Pakistan. The latest basketball cartoon element. 
Bigger thermal blockage. In fact, this lake real estate, the rhoncus ligula vestibulum, viverra risus. However, antioxidants chili element this time.
Stress arrows, but the convenience weekend impact. Each warm-up airline fears, but sad for malesuada vehicles. Stress developers who lion. 
Manufacturing, art organizations, reducing any need football, sauce a lorem. Pellentesque placerat nulla nec sem egestas cursus. 
Jasmine, but need to fear a hairstyle. Nulla.Stress protein or bow to fit consumer at the set. But the peanut sauce recipe and sad entrepreneurs drink prices. 
Financing need to chat, grab a lion, sauce temperature. Phasellus quis neque ullamcorper, vulputate than that, malesuada magna. 
But, for this, but something soft or customers as well as of vehicles. Textile innovative microwave enhanced. In order to receive the author, or the author of Performance now. 
Integer euismod massa id tristique hendrerit. Integer consectetur dolor dignissim Aenean, and the resume is porttitor quis. Is the chief and no players in the race. 
In order that the meaning that was. Tomorrow start or fear pull it. The lion's largest casino at real estate vehicles. Vestibulum lectus dolor, 
iaculis but out of hatred of life, porttitor Vestibulum consequat orci. Till et consectetuer laughter, the Bureau fears. Homework price enforcement pillow.'''

key_phrase_2 = key_phrase_2.lower()

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

#Encode/Decode a given message using key phrase 1 and key phrase 2
choice = input("\nWould you like to encode or decode a message: ").lower()
phrase = input("What is the phrase: ").lower()

# Removing all non letter from the users phrase
for non_letter in non_letters:
    phrase = phrase.replace(non_letter, '')

#For encoding
if choice == 'encode':
    encoded_phrase = []
    for letter in phrase:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)

    print("\nThe encoded message is: ")
    for letter in encoded_phrase:
        print(letter,end='')
#For decoding
elif choice == 'decode':
    decoded_phrase = []
    for letter in phrase:
        index = key_phrase_2_ordered_letters.index(letter)
        letter = key_phrase_1_ordered_letters[index]
        decoded_phrase.append(letter)

    print("\nThe decoded message is: ")
    for letter in decoded_phrase:
        print(letter, end='')
#User entered an invalid option
else:
    print("Please type 'encode' or 'decode'. Try again.")