names_list = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
name_counts = {}

for name in names_list:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

print(name_counts)

another_names_list = ["John", "Jane", "John", "Mike", "Jane", "John", "Sarah"]
another_name_counts = {}

for name in another_names_list:
    if name in another_name_counts:
        another_name_counts[name] += 1
    else:
        another_name_counts[name] = 1

print(another_name_counts)
