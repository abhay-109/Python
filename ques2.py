my_tuple = (15, 8, 23, 4, 42, 1, 30, 10, 7, 19)

print(f"The tuple is: {my_tuple}")

if not my_tuple:
    print("The tuple is empty.")
else:
    maximum_number = my_tuple[0]
    minimum_number = my_tuple[0]

    for number in my_tuple:
        if number > maximum_number:
            maximum_number = number
        if number < minimum_number:
            minimum_number = number

    print(f"The maximum number in the tuple is: {maximum_number}")
    print(f"The minimum number in the tuple is: {minimum_number}")
