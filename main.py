import random

secret_num = random.randint(1, 20)

turns = 0

while turns < 5:
    your_guess = int(input("Pick a number between 1 and 20: "))

    if your_guess > secret_num:
        if your_guess - secret_num <= 3:
            print("{} is larger, but it's very close!".format(your_guess))
        else:
            print("{} is larger than the secret number.".format(your_guess))
        turns += 1
        print("{}/5 turns used.".format(turns))

    elif your_guess < secret_num:
        if secret_num - your_guess <= 3:
            print("{} is smaller, but it's very close!".format(your_guess))
        else:
            print("{} is smaller than the secret number.".format(your_guess))
        turns += 1
        print("{}/5 turns used.".format(turns))

    else:
        print("Congratulations, you win the game!")
        break

if turns == 5:
    print("Sorry, you ran out of turns. The secret number was {}".format(secret_num))
