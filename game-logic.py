def play_game():
    print('welcom to the number guessing game!')
    random_number = generate_random_number()
    attemps =0
    while True:
        guess = get_user_input()
        attemps += 1
        if guess < random_number:
            print('too low! try again')
        elif guess > random_number:
            print('too high! try again')
        else:
            print(f'congratulations! you guessed the number in {attemps} attemps.')
            break