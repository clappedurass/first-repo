import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10. Can you guess it?")

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("What is your guess? "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in " + str(attempts) + " attempts!")
            break
    except ValueError:
        print("Please enter a valid number.")
