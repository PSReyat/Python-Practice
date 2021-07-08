#First exercise

prices = [10, 20, 30]
total_price = 0

for items in prices:
    total_price += items

print(f"total price of objects: {total_price}")

#Second exercise

numbers = [5, 2, 5, 2, 2]

for x in numbers:
    output = ""
    for y in range(x):
        output += "x"

    print(output)

#Third exercise - Finding biggest value in a list.

list1 = [7, 5, 3, 8, 6, 1, 3, 4, 6, 8, 9, 10, 1, 4, 5, 6, 4, 3, 2, 1]
largest = 0;

for item1 in list1:
    largest = item1
    for item2 in list1:
        if item2 > largest:
            largest = item2

print(f"Largest = {largest}")

#Fourth exercise - removing duplicates from a list

list2 = [7, 5, 3, 8, 6, 1, 3, 4, 6, 8, 9, 10, 1, 4, 5, 6, 4, 3, 2, 1]
uniqueList = [];

for items in list2:
    if not uniqueList.__contains__(items):
        uniqueList.append(items)

print(uniqueList)