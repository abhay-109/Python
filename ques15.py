numbers = []

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")
    if user_input == 'done':
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

if not numbers:
    print("No numbers were entered.")
else:
    largest_number = numbers[0]
    smallest_number = numbers[0]

    for num in numbers:
        if num > largest_number:
            largest_number = num
        if num < smallest_number:
            smallest_number = num

    print(f"The entered list is: {numbers}")
    print(f"The largest number is: {largest_number}")
    print(f"The smallest number is: {smallest_number}")
