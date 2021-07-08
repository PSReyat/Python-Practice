target = 9
guess_count = 1
guess_limit = 5

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess_count == guess_limit:
        print("You lost...")
        break
    if guess < target:
        print("A bit higher")
    elif guess > target:
        print("A bit lower")
    else:
        print("Correct!")
