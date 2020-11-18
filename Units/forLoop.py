# 1st looping through a list of elements with a for loop
print("=======================")
teams = ["giants", "bills", "jet", "patriots"]

for i in teams:
    print(i.title())
print("=======================")

values = [1, 2, 3, 4, 5]
total_sum = 0
for value in values:
    total_sum += value
print(total_sum)
print("=======================")

triples = [["a", "b", "c"], ["1", "2", "3"], ["do", "re", "me"]]
for list_value in triples:
    for element in list_value:
        print(element, end=' ')
print("\n=======================")

# 2nd Looping Through a Numerical Range

num_val = range(1, 10)
print(num_val)
print(type(num_val))
print("=======================")

for i in range(1, 11):
    print(i)
print("=======================")

for num in range(5):
    print(num)
print("=======================")

for i in range(2, 11, 2):
    print(i)
print("=======================")

word = "Hello World"
list_word = list(word)
print(word)
print(list_word)
print("=======================")
list_word[5] = "NEW"
print(list_word)
print("=======================")

numbers = list(range(10, 101, 10))
print(numbers)
print("=======================")

for number in numbers:
    print(number)
print("=======================")

squares = []
for num_val in numbers:
    square = num_val**2
    squares.append(square)
print("Populating squares Complete")
print("=======================")

for square in squares:
    print(square)
print("=======================")

print("Populating Cubes Complete")
print("=======================")
cubes = [num_val**3 for num_val in numbers]
for cube in cubes:
    print(cube)
print("=======================")

print(min(cubes))
print(max(cubes))
print(sum(cubes))

print("=======================")
