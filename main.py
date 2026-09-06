import random

def choose_difficulty():
    while True:
        try:
            difficulty = int(input("Choose difficulty: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if difficulty == 1:
            secret_number = random.randint(1, 50)
            max_attempts = 10
        elif difficulty == 2:
            secret_number = random.randint(1, 100)
            max_attempts = 7
        elif difficulty == 3:
            secret_number = random.randint(1, 500)
            max_attempts = 5
        else:
            print("Invalid Choice!")
            continue
        return secret_number, max_attempts

def play_game(secret_number, max_attempts):
    count = 0
    won = False

    while count < max_attempts:
        try:
            guess = int(input("Enter Your Guess :"))
            count += 1
        except ValueError:
            print("Please enter a valid number")
            continue

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print("Correct! You guessed the number in", count, "Attempts!")
            won = True
            break
    if not won:
        print(f"Game over! You ran out of attempts.\nThe number was {secret_number}")

def ask_to_play_again():
    while True:
        play_again = input("Play again? (y/n): ")

        if play_again == "y":
            return True

        elif play_again == "n":
            return False

        else:
            print("Please Enter y or n")

while True:
    secret_number, max_attempts = choose_difficulty()
    play_game(secret_number, max_attempts)

    play_again = ask_to_play_again()

    if not play_again:
        break