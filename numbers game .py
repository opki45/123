import random
number = random.randrange(1,1000)
guess = int(input("Enter any number: "))
while guess != number:
    if guess < number:
        print("Guess is too low")
        guess = int(input("Enter another number: "))
    elif guess > number:
        print("Guess is too high")
        guess = int(input("Enter another number"))
    else:
        break
print("You guessed the right number: ")