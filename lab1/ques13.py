number = 5
factorial = 1

if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    current_num = 1
    while current_num <= number:
        factorial *= current_num
        current_num += 1
    print(f"The factorial of {number} is {factorial}.")

number_2 = 7
factorial_2 = 1

if number_2 < 0:
    print("Factorial does not exist for negative numbers.")
elif number_2 == 0:
    print("The factorial of 0 is 1.")
else:
    current_num_2 = 1
    while current_num_2 <= number_2:
        factorial_2 *= current_num_2
        current_num_2 += 1
    print(f"The factorial of {number_2} is {factorial_2}.")
