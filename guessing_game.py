target = 9

guess = int(input("Guess: "))

while guess is not target:
    if guess < target:
        print("A bit higher")
    elif guess > target:
        print("A bit lower")
    guess = int(input("Guess: "))

print("Correct!")