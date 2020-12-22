from matplotlib import pyplot


# Loan Calculator App

def get_loan_info():
    """Get the basic information of a loan and store it in a dictionary"""

    # Create a blank dist to represent a loan
    loan = {}

    # Get user input for the categories of the loan
    loan['principal'] = float(input("\nEnter the loan amount: "))
    loan['rate'] = float(input("Enter the interest rate: ")) / 100
    loan['monthly payment'] = float(input("Enter the desired monthly payment amount: "))
    loan['money paid'] = 0

    return loan


def show_loan_info(loan, number):
    """Display the current loan status"""
    print("\n-----Loan information after " + str(number) + " months-----")
    for key, value in loan.items():
        print(key.title() + ": " + str(value))


def collect_interest(loan):
    """Update loan for interest per month"""
    loan['principal'] = loan['principal'] + loan['principal'] * loan['rate'] / 12


def make_monthly_payment(loan):
    """Simulate making a monthly payment to pay down the principal"""
    loan['principal'] = loan['principal'] - loan['monthly payment']
    if loan['principal'] > 0:
        loan['money paid'] += loan['monthly payment']
    else:
        loan['money paid'] += loan['monthly payment'] + loan['principal']
        loan['principal'] = 0


def summarize_loan(loan, number, initial_principal):
    """Display the results of paying off the loan"""
    print("\nCongratulations! You paid off your loan in " + str(number) + " months!")
    print("Your initial loan was $" + str(initial_principal) + " at a rate of " + str(100 * loan['rate']) + "%.")
    print("Your monthly payment was $" + str(loan['monthly payment']) + ".")
    print("You spent $" + str(round(loan['money paid'], 2)) + " in total.")

    interest = round(loan['money paid'] - initial_principal, 2)
    print("You spent $" + str(interest) + " on interest!")


def create_graph(data, loan):
    """Create a graph to show the relationship between principal and time"""
    x_value = []  # month number
    y_value = []  # principal value

    # Loop through data set. Point is a tuple.
    # point[0] represents a month number,
    # point[1] represents a principal value
    for point in data:
        x_value.append(point[0])
        y_value.append(point[1])

    # Create a plot for x value and y value
    pyplot.plot(x_value, y_value)
    pyplot.title(str(100 * loan['rate']) + "% interest with $" + str(loan['monthly payment']) + " Monthly Payment.")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()


# The main code
print("Welcome to the Loan Calculator App")
month_number = 0

my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []

show_loan_info(my_loan)
print("Press Enter to begin paying off your loan.")
