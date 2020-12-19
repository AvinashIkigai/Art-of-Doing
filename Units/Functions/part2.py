def hello_world(name, age):
    """Greet the whole world"""
    print("Hello " + name.title() + "!")
    print("You are " + str(age) + " years old.")

hello_world("mike",25)

def goodbye_world(name='nobody', day='today'):
    """Say Goodbye to a person"""
    print("Goodbye " + name.title() + "...")
    print("May you have a good " + day.title() + ".")

goodbye_world()
goodbye_world('mike')
goodbye_world('mike' , 'friday')

def calc_age(age=0, interval=10):
    """Calculate a persons age in x years."""
    print("You are currently " + str(age) + " years old.")
    age += interval
    print("In " + str(interval) + " years you will be " +str(age)+".")
calc_age()
calc_age(33)
calc_age(33,22)