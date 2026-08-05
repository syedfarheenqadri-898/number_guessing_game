#NUMBER GUESSING GAME
import random
secret_number = random.randint(1, 100)
print("===== Number Guessing Game =====")
print("I have chosen a number between 1 and 100.")
print("You have 5 attempts to guess it.")
for attempt in range(1, 6):
    while True:
        guess = input(f"\nAttempt {attempt}: Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            # Check if the number is within the valid range
            if 1 <= guess <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Please enter a valid number.")

    if guess == secret_number:
        print(" Congratulations! You guessed the correct number.")
        print(f"You guessed it in {attempt} attempt(s).")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    remaining = 5 - attempt
    if remaining > 0:
        print(f"You have {remaining} attempt(s) left.")

else:
    print("\n OOPS! Game Over!")
    print(f"The correct number was {secret_number}.")