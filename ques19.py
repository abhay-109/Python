print("Armstrong numbers between 100 and 999:")

number = 100
while number <= 999:
    original_number = number
    sum_of_cubes = 0

    digit1 = original_number % 10
    remaining_number = original_number // 10
    digit2 = remaining_number % 10
    digit3 = remaining_number // 10

    sum_of_cubes += digit1 * digit1 * digit1
    sum_of_cubes += digit2 * digit2 * digit2
    sum_of_cubes += digit3 * digit3 * digit3

    if sum_of_cubes == original_number:
        print(original_number)

    number += 1
