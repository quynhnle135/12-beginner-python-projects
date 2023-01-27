import random


def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    guess_number = int(input(f"Guess a number between 1 and {x}: "))
    while guess_number != random_number:
        if guess_number < random_number:
            guess_number = int(input("A little lower that expected. Guess again please: "))
        else:
            guess_number = int(input("Kinda bigger than expected. Please guess again: "))
    print(f"Congratulations! You have guessed the {guess_number} correctly!!!")


guess(10)



