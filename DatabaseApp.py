print("Welcome to the Database Admin Program")

#Create a dictionary to hold all username:password key-value pairs
log_on_information = {
    'moonman74':'avinash@123',
    'merymo1986':'avinash@123',
    'nikcyD':'avinash@123',
    'george2':'avinash@123',
    'admin':'admin123'
}
#Get user input
username = input("Enter your username: ")
#Simulate logging on...
#Get user password
if username in log_on_information.keys():
    password = input("Enter youe password: ")
    if password == log_on_information[username]:
        print("\nHello "+ username + "! You are logged in!")
        if username == 'admin':
            #Show the whole database
            print("\nHere is the current user database:")
            for key, value in log_on_information.items():
                print("Username: " + key + "\t\tPassword: " + value)
        else:
            #Allow standard user to change their password
            password_change = input("Would you like to change your password (yes/no): ").lower().strip()
            if password_change == 'yes':
                new_password = input("What would you like your new password to be (min 8 chars): ")
                if len(new_password) >= 8:
                    log_on_information[username] = new_password
                else:
                    print(new_password + "is not the minimum 8 characters.")
                print("\n" + username + " your password is " + log_on_information[username] +".")
            else:
                print("\nThank You,Goodbye.")
    else:
        print("Password incorrect!")
else:
    print("Username not in database. Goodbye.")