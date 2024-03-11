# Viviyan Tsaneva - Capstone Project T05
# This program allows the user to access two different financial calculators.
# One calculates the simple or compound interest on an investment, and the other the amount to pay on a home loan.

import math

# Provide user with calculator options and prompt them to choose.
print('''Welcome to our financial calculators! You can find bellow the types of calculators we offer:
investment - to calculate the amount of interest you'll earn on your investent
bond       - to calculate the amount you'll have to pay on a home loan''')

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
user_choice_lower = user_choice.lower()  # Ensure valid user input remains valid regardless of how the user capitalises.  

# Calculate interest on investment.
if user_choice_lower == 'investment':
    P = float(input('Enter the amount of money you are depositing:'))
    r = float(input('Enter your interest rate (number only):'))/100
    t = int(input('Enter the number of years you plan on investing with us:'))
    interest = input('Do you want to check your simple or compound interest:')
    if interest.lower() == 'simple':
        simple_interest_total = P*(1+r*t)
        print("Your total after the simple interest is:", round(simple_interest_total,2))        
    elif interest.lower() == 'compound':
        compound_interest_total = P*math.pow((1+r),t)
        print("Your total after the compound interest is:", round(compound_interest_total,2))    
    else:
        print("Invalid input. Enter 'simple' or 'compound'.")

# Calculate amount to pay on a home loan.
elif user_choice_lower == 'bond':
   P = float(input("Enter the present value of the house:"))
   i_monthly = (float(input("Enter the yearly interest rate:"))/100)/12
   n = int(input("Enter the number of months you plan to take to repay:"))
   repayment = (i_monthly*P)/(1 - (1 + i_monthly)**(-n))
   print("Your monthly repayment amount is:",round(repayment,2))
else:
    print("Invalid input. Enter 'investment' or 'bond'")