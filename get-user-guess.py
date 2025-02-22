def get_user_input():
    while True:
        try:
            guess = int(input('enter your guess (1-100):'))
            if guess >= 1 and guess <=100:
                return guess
            else:
                print('please enter a number between 1 and 100')

        except ValueError:
            print('invalid input! please enter a number')

get_user_input()