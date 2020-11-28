#Dictionaries

bob_info = {
    'first_name':'Bob',
    'last_name':'Jones',
    'age':27,
    'fav_colors':['green','orange']
    }

print(bob_info)
print(type(bob_info))

print(bob_info['age'])
print(bob_info['fav_colors'][0])

bob_info['weight'] = 180
bob_info['height'] = 72.6
print(bob_info)

bob_info['weight'] -= 5
print(bob_info['first_name']+":" + str(bob_info['weight']))

bob_info['age'] += 1
print("Happy birthday " + bob_info['first_name'] + "! You are now " + str(bob_info['age']))

del bob_info['fav_colors']
print(bob_info)

# user_info = {}
# user_info['name'] = input('\nWhat is your name: ').title()
# user_info['age'] = input("What is your age: ")
# user_info['job'] = input("Enter your job title: ").title()
#
# print(user_info)

fav_colors = {
    'john':'blue',
    'gabe':'orange',
    'mary':'yellow',
    'lucus':'purple',
    'mike':'yellow',
    'sarah':'green'
}
print(fav_colors)
fav_colors_list = fav_colors.items()
print(fav_colors_list)

for key, value in fav_colors.items():
    print("The key " + key.title() +" has associated value of " + value.title() +".")
print("")
fav_colors_key = fav_colors.keys()
print(fav_colors_key)

for key in fav_colors.keys():
    print(key.title() + ",thank you for taking the survey")
if 'brooke' not in fav_colors.keys():
    print("Brooke, you should take the survey.\n")

fav_colors_value = fav_colors.values()
print(fav_colors_value)
print("\nThe colors voted on were: ")
for value in set(fav_colors.values()):
    print(value)
print("*******************\n")
#Nesting Dictionaries

user_0 = {
    'name':'john',
    'age':22,
}
user_1 = {
    'name':'bill',
    'age':27,
}
user_2 = {
    'name':'mary',
    'age':31,
}

users = [user_0, user_1, user_2]

for user in users:
    for key,value in user.items():
        print(key.title()+": " + str(value))
    print("\n")
users = []
for user in range(100):
    new_user = {'name':'NA', 'age':0}
    users.append(new_user)

for user in users[:10]:
    print(user)

friends = {
    'bill':['john','tom','mary'],
    'tom':['john','bill','sue'],
    'mary':['sue','bill','tom'],
}
for key,values in friends.items():
    print("\n"+ key.title() + "'s friends are: ")
    for value in values:
        print("\t" + value.title())

user_directory = {
    'msmith':{
        'first_name':'mark',
        'last_name':'smith',
        'age':27,
    },
    'ejones':{
        'first_name':'eddie',
        'last_name':'jones',
        'age':42,
    },
}
for user, info in user_directory.items():
    print("\nUsername: "+ user)
    for key, value in info.items():
        print(key + ": " + str(value))