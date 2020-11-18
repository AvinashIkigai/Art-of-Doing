# List Slicing

numbers = list(range(1, 11))
for num in numbers:
    print(num)
print("=======================")
print("\nSlicing")
for num in numbers[0:5]:
    print(num)
print("=======================")

for num in numbers[5:]:
    print(num)
print("=======================")
new_numbers = numbers
print(numbers)
print(new_numbers)
print("=======================")
numbers.pop()
print(numbers)
print(new_numbers)
print("=======================")

numbers = list(range(1, 6))
print(numbers)
print("=======================")

new_numbers = numbers[:]
print(numbers)
print(new_numbers)
print("=======================")
numbers.pop()
print(numbers)
print(new_numbers)
print("=======================")

names = ["john", "bill", "mary"]
new_names = names.copy()
print(names)
print(new_names)
print("=======================")

# The Zip Function

players = ["jack", "john", "mark", "bill"]
jersey_nums = [20, 44, 3, 14]

# for player in players:
#     print(player)
# print("=======================")

# for jersey_num in jersey_nums:
#     print(jersey_num)
# print("=======================")

for i in range(len(players)):
    print(players[i].title() + ": " + str(jersey_nums[i]))
print("=======================")

for player, jersey_num in zip(players, jersey_nums):
    print(player.title() + ": " + str(jersey_num))
print("=======================")
