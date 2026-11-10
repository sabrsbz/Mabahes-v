import random

MIN_NUM = 1
MAX_NUM = 100
MAX_TRIES = 10

secret = random.randint(MIN_NUM, MAX_NUM)

print(f"I'm thinking of a number between {MIN_NUM} and {MAX_NUM}.")
print(f"You have {MAX_TRIES} attempts to guess it.\n")

won = False

for attempt in range(1, MAX_TRIES + 1):
    # Get a valid integer from the user
    while True:
        try:
            guess = int(input(f"Guess #{attempt}: "))
            break
        except ValueError:
            print("Please enter a whole number.")

    if guess == secret:
        print(f"\nCongratulations! The number was {secret}, and you won in {attempt} attempt(s).")
        won = True
        break
    elif guess < secret:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    print(f"Attempts left: {MAX_TRIES - attempt}\n")

if not won:
    print(f"You lost! The number was {secret}.")
