# program for calculating annuity payment

# imports
import math
import argparse

# get arguments with argparse

parser = argparse.ArgumentParser(description='Annuity payment calculator')
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float)

# parse values to 'args'
args = parser.parse_args()

# functions
# function to calculate number of monthly payments


def calculate_number_of_monthly_payments(principal, payment, interest):
    # calculate nominal interest rate as 'i'
    i = (interest / 100) * (1/12)

    # calculate number of months as 'n'
    n = math.log(payment / (payment - i * principal), 1 + i)

    # round it up
    n = math.ceil(n)

    # convert to more readable format ie years & months
    number_of_years = n // 12
    number_of_months = math.ceil(n % 12)

    # display
    # check if number of years or months is 0
    if number_of_years == 0:
        print(f'It will take {number_of_months} months to repay this loan!')
    elif number_of_months == 0:
        print(f'It will take {number_of_years} years to repay this loan!')
    else:
        print(f'It will take {number_of_years} years and {number_of_months} months to repay this loan!')


# function to calculate the monthly payment ie annuity payment


def calculate_monthly_payment(principal, periods, interest):
    # calculate nominal interest rate as 'i'
    i = (interest / 100) * (1 / 12)

    # calculate monthly payment
    monthly_payment = principal * ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))

    # display monthly payment
    print(f'Your monthly payment = {math.ceil(monthly_payment)}!')


# function to calculate loan principal


def calculate_loan_principal(payment, periods, interest):
    # calculate nominal interest rate as 'i'
    i = (interest / 100) * (1 / 12)

    # calculate loan principal
    loan_principal = payment / ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))

    # display
    print(f'Your loan principal = {round(loan_principal)}!')


# compute according to given flags
if args.periods is None:
    calculate_number_of_monthly_payments(args.principal, args.payment, args.interest)
elif args.payment is None:
    calculate_monthly_payment(args.principal, args.periods, args.interest)
else:
    calculate_loan_principal(args.payment, args.periods, args.interest)
