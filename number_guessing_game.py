##Build a number guessing game where there is a target number the user must find it, when the user enter a number,
##you must indicate if the desired one is less or more than the input, the user has 10 attempts, 
##if he did not find the number within those attempts, he loses, if he finds it he wins, you should put that in a function.
##Note: you can use the library random to generate the target number or you can simply put it manually in your code.

import random

def number_guessing(target):
    attempts = 10
    while attempts > 0:
        guess = int(input("Enter a number between 1 and 30: "))
        if guess > target:
            print("This number is big try again!")
        elif guess < target:
            print("This number is small try again!")
        else:
            print(" nste3ref bik ! You found the number.")
            return True
            break 
        attempts -= 1
    
    print("Sorry, you didn't find the number. The number was " + str(target))
    return False


