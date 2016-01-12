from random import randrange

#This program generates a number between 1 and 10, and has the user guess what it is until they get it right on
rand = randrange(0,10)  #random int generated
guess = int(input("Guess a number between 0 and 10: "))  #integer input from user
answerCorrect = False  #boolean for controlling the while loop

while answerCorrect == False:  #loop goes on until the user gets the answer right, at which point the boolean
    if guess > rand:           #becomes true and stops the loop
        print("Too High!")
        guess = int(input("Try again: "))
    if guess < rand:
        print("Too Low!")
        guess = int(input("Try again: "))
    else:
        answerCorrect = True
        print("Right on!")





