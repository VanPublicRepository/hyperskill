import random

# get number of friends
number_of_friends = int(input("Enter the number of friends joining (including you):"))

# check for invalid input
if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    # create dictionary and fill it
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}

    for i in range(number_of_friends):
        name = input()
        friends[name] = 0

    # print(friends)

    # get bill value
    bill_value = float(input('Enter the total bill value: '))

    # implement lucky feature
    lucky_feature = input('Do you want to use the "Who is lucky?" feature?\nWrite Yes/No:')
    if lucky_feature == 'Yes':
        # pick random name from dictionary
        lucky_num = random.randint(1, number_of_friends)  # where 1 -> number_of_friends represent indices
        # print(lucky_num)
        index = 1
        for friend in friends:
            if lucky_num == index:
                lucky_one = friend
            else:
                index += 1
        print(f'{lucky_one} is the lucky one!')
        
        # update lucky_one to zero while re-splitting the bill
        paid_amount = round(bill_value / (number_of_friends - 1), 2)

        # update dictionary and print it
        for friend in friends:
            if friend == lucky_one:
                friends[friend] = 0
            else:
                friends[friend] = paid_amount

    else:
        print('No one is going to be lucky')
        # divide among friends
        paid_amount = round(bill_value / number_of_friends, 2)

        # update dictionary and print it
        for friend in friends:
            friends[friend] = paid_amount

        print(friends)
