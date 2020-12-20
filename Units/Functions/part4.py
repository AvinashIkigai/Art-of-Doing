#Local and Global variable

def times_ten(x):
    x *= 10
    print(x)

def char_replace(word):
    while 'a' in word:
        word = word.replace('a','@')
    while 'e' in word:
        word = word.replace('e','3')
    while 'i' in word:
        word = word.replace('i','!')
    while 'o' in word:
        word = word.replace('o','0')
    while 'u' in word:
        word = word.replace('u','#')
    return word

number = 3
times_ten(number)

phrase = "Hello How are you doing today?"
phrase = char_replace(phrase)
print(phrase)