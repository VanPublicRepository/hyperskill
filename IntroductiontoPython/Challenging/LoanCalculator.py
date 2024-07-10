# program for calculating annuity payment

# imports
import math
import argparse

# get arguments with argparse

parser = argparse.ArgumentParser(description='Annuity payment calculator')
parser.add_argument('--type')
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

    # calculate and display overpayment
    overpayment = n * math.ceil(payment) - principal

    # ceil it
    overpayment = math.ceil(overpayment)

    # display
    print(f'Overpayment = {overpayment}')

# function to calculate the monthly payment ie annuity payment


def calculate_monthly_payment(principal, periods, interest):
    # calculate nominal interest rate as 'i'
    i = (interest / 100) * (1 / 12)

    # calculate monthly payment
    monthly_payment = principal * ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))

    # display monthly payment
    print(f'Your monthly payment = {math.ceil(monthly_payment)}!')

    # calculate and display overpayment
    overpayment = periods * math.ceil(monthly_payment) - principal

    # ceil it
    overpayment = math.ceil(overpayment)

    # display
    print(f'Overpayment = {overpayment}')


# function to calculate loan principal


def calculate_loan_principal(payment, periods, interest):
    # calculate nominal interest rate as 'i'
    i = (interest / 100) * (1 / 12)

    # calculate loan principal
    loan_principal = payment / ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))

    # display
    print(f'Your loan principal = {round(loan_principal)}!')

    # calculate and display overpayment
    overpayment = periods * payment - loan_principal

    # ceil it
    overpayment = math.ceil(overpayment)

    # display
    print(f'Overpayment = {overpayment}')


# function to calculate differentiated payment


def calculate_differentiated_payment(principal, periods, interest):
    # calculate nominal interest rate as 'i'
    i = (interest / 100) * (1 / 12)

    sum_of_differentiated_payments = 0

    # repeat for given periods
    for m in range(1, int(periods + 1)):
        # calculate differentiate payment
        d = (principal / periods) + i * (principal - ((principal * (m - 1)) / periods))

        # ceil it
        d = math.ceil(d)

        # sum required for overpayment calculation
        sum_of_differentiated_payments += d

        # display
        print(f'Month {m}: payment is {d}')

    # calculate and display overpayment
    overpayment = sum_of_differentiated_payments - principal

    # ceil it
    overpayment = math.ceil(overpayment)

    # display
    print()
    print(f'Overpayment = {overpayment}')


# compute according to given flags and check for invalid input
if args.type == 'diff':
    if args.payment is None:
        if args.principal is None or args.periods is None or args.interest is None:
            print('Incorrect parameters')
        elif args.principal < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            calculate_differentiated_payment(args.principal, args.periods, args.interest)
    else:
        print('Incorrect parameters')
elif args.type == 'annuity':
    if args.interest is None:
        print('Incorrect parameters')
    else:
        if args.periods is None:
            if args.principal is None or args.payment is None or args.interest is None:
                print('Incorrect parameters')
            elif args.principal < 0 or args.payment < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calculate_number_of_monthly_payments(args.principal, args.payment, args.interest)
        elif args.payment is None:
            if args.principal is None or args.periods is None or args.interest is None:
                print('Incorrect parameters')
            elif args.principal < 0 or args.periods < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calculate_monthly_payment(args.principal, args.periods, args.interest)
        else:
            if args.payment is None or args.periods is None or args.interest is None:
                print('Incorrect parameters')
            elif args.payment < 0 or args.periods < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calculate_loan_principal(args.payment, args.periods, args.interest)
else:
    print('Incorrect parameters')
