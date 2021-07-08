target = 9

guess = int(input("Guess: "))
count = 1

while guess is not target:
    if guess < target:
        print("A bit higher")
    elif guess > target:
        print("A bit lower")
    elif guess is target:
        print("Correct!")
        break
    guess = int(input("Guess: "))
    count = count + 1
    if count == 5:
        print("You lost...")
        break

