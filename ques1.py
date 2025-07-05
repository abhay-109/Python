my_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_elements = []
for item in my_list:
    if item not in unique_elements:
        unique_elements.append(item)
print(unique_elements)

another_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
unique_fruits = []
for item in another_list:
    if item not in unique_fruits:
        unique_fruits.append(item)
print(unique_fruits)
