weight = input("What's your weight? ")
unit = input("Lbs (L/l) or KG (K/k)? ")

convert = int(weight)

if unit == "L" or unit == "l":
    convert = convert/2.2
    print(f"You are {convert}kg")
elif unit == "K" or unit == "k":
    convert = convert * 2.2
    print(f"You are {convert} pounds")
