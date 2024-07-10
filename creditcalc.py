import math

# get loan principle
print('Enter the loan principal:')
loan_principle = int(input())

# get type of payment input
print('What do you want to calculate?')
print('type "m" for number of monthly payments,')
print('type "p" for the monthly payment:')

payment_type = input()

# if m than calculate number of monthly payments
if payment_type == 'm':
    print('Enter the monthly payment:')

    # get monthly payment
    input_monthly_payment = int(input())

    # calculate time for monthly payments
    time_for_payment = loan_principle / input_monthly_payment

    # check for grammar ie singular or plural
    if math.ceil(time_for_payment) == 1:
        print(f'It will take {math.ceil(time_for_payment)} month to repay the loan')
    else:
        print(f'It will take {math.ceil(time_for_payment)} months to repay the loan')

else:
    # get number of months
    print('Enter the number of months:')
    number_of_months = int(input())

    # calculate monthly payment
    calculated_monthly_payment = loan_principle / number_of_months

    # check if calculated monthly payment is a float or not
    # if float then calculate last payment
    if calculated_monthly_payment == math.ceil(calculated_monthly_payment):  # it is not a decimal number
        # display the monthly payment
        print(f'Your monthly payment = {math.ceil(calculated_monthly_payment)}')
    else:
        # calculate last payment
        last_payment = loan_principle - (number_of_months - 1) * math.ceil(calculated_monthly_payment)

        # display
        print(f'Your monthly payment = {math.ceil(calculated_monthly_payment)} and the last payment = {last_payment}')
