import random

secret_num = int(input("Pick a number between 1 and 20: "))

turns = 0

low = 1
high = 20

while turns < 5:
    computer_guess = random.randint(low, high)

    if computer_guess > secret_num:
        if computer_guess - secret_num <= 3:
            print("{} is larger, but it's close!".format(computer_guess))
        else:
            print("{} is larger than the secret number.".format(computer_guess))
        turns += 1
        print("{}/5 turns used.".format(turns))
        high = computer_guess - 1

    elif computer_guess < secret_num:
        if secret_num - computer_guess <= 3:
            print("{} is smaller, but it's very close!".format(computer_guess))
        else:
            print("{} is smaller than the secret number.".format(computer_guess))
        turns += 1
        print("{}/5 turns used.".format(turns))
        low = computer_guess + 1

    else:
        print("I win the game!")
        break

if turns == 5:
    print("Noooo, I ran out of turns.")
