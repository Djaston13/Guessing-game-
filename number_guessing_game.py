import random

def number_guessing_game():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"✅ Correct! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("❌ Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
