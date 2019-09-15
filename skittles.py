'''
This program generates a random number of skittles from 0 to 1023 and repeatedly
ask the user to guess until they get it correctly.
---Program written by Son Nguyen---
'''
#Import the random python library
import random

#Define the minimum and maximum amount of skittles
MIN_SKITTLES = 0
MAX_SKITTLES = 1023

#Generate a random number between min and max and prompt the user for a guess
num_skittles = random.randint(MIN_SKITTLES, MAX_SKITTLES)
print(num_skittles)
user_guess = int(input("Guess how many skittles we have: "))

#Repeat the prompt the guess is not equivalent to the random skittles amount
while user_guess != num_skittles:
    print(user_guess)
    if(user_guess > num_skittles):
        user_guess = int(input("Too high. Try again: "))
    else:
        user_guess = int(input("Too low. Try again: "))

#Notify the user that they won and thank them for playing
print("You got it! We have: " + str(num_skittles))
print("Thank you for playing.")

