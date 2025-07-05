dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}

merged_dict = dict1.copy()

for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value

print(merged_dict)

dict3 = {'x': 100, 'y': 200}
dict4 = {'y': 50, 'z': 150}

merged_dict2 = dict3.copy()

for key, value in dict4.items():
    if key in merged_dict2:
        merged_dict2[key] += value
    else:
        merged_dict2[key] = value

print(merged_dict2)
