import random


def computer_guess(x):
    print(f"Let the computer guess a number between 1 and {x}")
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ")
        if feedback == 'l':
            low = guess + 1
        else:
            high = guess - 1
    print("Yasss! The computer has just guessed the correct number!!!")


computer_guess(10)