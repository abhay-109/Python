list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]

result_list = []

for item1 in list1:
    is_present_in_list2 = False
    for item2 in list2:
        if item1 == item2:
            is_present_in_list2 = True
            break
    if not is_present_in_list2:
        result_list.append(item1)

print(result_list)

names1 = ["Alice", "Bob", "Charlie", "David"]
names2 = ["Bob", "Eve", "Charlie"]

result_names = []

for name1 in names1:
    is_present_in_names2 = False
    for name2 in names2:
        if name1 == name2:
            is_present_in_names2 = True
            break
    if not is_present_in_names2:
        result_names.append(name1)

print(result_names)
