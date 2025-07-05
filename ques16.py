positive_count = 0
negative_count = 0
zero_count = 0

print("Please enter 10 integers:")

current_input_count = 0
while current_input_count < 10:
    try:
        number = int(input(f"Enter integer {current_input_count + 1}: "))
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1
        current_input_count += 1
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeroes: {zero_count}")
