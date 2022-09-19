from random import randint
from sys import exit

number = randint(1, 100)
guesses = 0

while True:
    guess = input("Choose a number between 1 - 100\n> ")
    guesses += 1
    if int(guess) == number:
        if guesses == 1:
            print("FIRST TRY! THAT 1 in a 100 chance! WOW!")
        else:
            print("You got it! Good job!")
        exit()
    if int(guess) < number:
        print("Higher, guess again!")
    if int(guess) > number:
        print("Lower, guess again!")

