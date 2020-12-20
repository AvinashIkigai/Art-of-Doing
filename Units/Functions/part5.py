
def remove_name(names):
    """"Remove a name from a list"""
    removed_name = names.pop()
    print("Goodbye " + removed_name.title() +".")

friends = ['john', 'jack', 'jill', 'james']
remove_name(friends.copy())

