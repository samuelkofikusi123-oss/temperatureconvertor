import random # this is responsible for the random numbers
secret = random.randint (1,10) # the integer indicates the range of the randon number
guess = 0 #this changes the more you guess a number
attempts = 0 # this indicates the number of attempts you have
while guess != secret: # the while keeps the questioning going till you get it right
    guess = int(input("Guess a number between 1 and 10: "))
    attempts = attempts + 1
    if guess < secret:
        print("Too low, guess something higher ") # i think this is self explanatory

    elif guess > secret:
        print("Too high, guess something lower") #i think this is self explanatory

    else:
        print("Correct!, great job") #i think this is self explanatory