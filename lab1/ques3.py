my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for number in my_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

another_set_of_numbers = [11, 22, 33, 44, 55, 66]
even_numbers_from_another_list = []
for number in another_set_of_numbers:
    if number % 2 == 0:
        even_numbers_from_another_list.append(number)
print(even_numbers_from_another_list)
