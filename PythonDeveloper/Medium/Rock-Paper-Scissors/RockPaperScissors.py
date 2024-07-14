
# rock-paper-scissor game

# imports
import random

# functions


# function to get random computer choice
def generate_computer_choice(user_options):
    computer_choice_list = user_options

    random_index = random.randint(0, len(computer_choice_list) - 1)
    computer_random_choice = computer_choice_list[random_index]

    return computer_random_choice


# function to get score from rating.txt
def get_user_score():
    # get name and check if in rating.txt for score
    user_name = input('Enter your name: ')

    # greeting
    print(f'Hello, {user_name}')

    # checking for score
    file = open('rating.txt', 'r')

    # default score
    user_score = 0

    for line in file:
        # get the name in line
        # remove /n character
        line = line.strip()

        # check for name
        line_list = line.split(' ')
        if line_list[0] == user_name:
            user_score = int(line_list[1])

    file.close()
    return user_score


# function for game state
def game_loop(score, options):
    while True:
        # get user choice and generate computer choice
        user_choice = input()
        computer_choice = generate_computer_choice(options)

        # main if branch for deciding win, draw, or loss and adding score
        if user_choice == '!exit':
            print('Bye!')
            break
        elif user_choice == '!rating':
            print(f'Your rating: {score}')
        elif user_choice in options:
            score = check_for_result(score, options, user_choice, computer_choice)
        else:
            print('Invalid input')


# function to get the list of options
def get_list_of_options():
    options_list = input().split(',')

    if options_list[0] == '':  # default
        options_list = ['rock', 'paper', 'scissors']

    print('Okay, let\'s start')
    return options_list


# function to check for win, draw, or lose
def check_for_result(score, options, user_choice, comp_choice):

    # make a list for options excluding user_choice
    previous_list = []  # options before user_choice
    forward_list = []   # option after user_choice

    flag = False  # flag for if word appeared
    for word in options:
        if word != user_choice and flag is False:
            previous_list.append(word)

        if flag is True:
            forward_list.append(word)

        if word == user_choice:
            flag = True

    list_for_winning = forward_list + previous_list

    # split the list into first half -> list beats choice
    # split the list into second half -> choice beats list

    first_half_list = list_for_winning[:len(list_for_winning)//2]
    second_half_list = list_for_winning[len(list_for_winning)//2:]

    # check for win, lose, or draw
    if comp_choice in first_half_list:
        print(f'Sorry, but the computer chose {comp_choice}')
        return score
    elif comp_choice in second_half_list:
        score += 100
        print(f'Well done. The computer chose {comp_choice} and failed')
        return score
    elif comp_choice == user_choice:
        score += 50
        print(f'There is a draw ({comp_choice})')
        return score
    else:
        print('Invalid input')
        return score


# main
game_loop(get_user_score(), get_list_of_options())
