input_string = "hello world"
char_counts = {}

for char in input_string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print(char_counts)

another_string = "programming is fun"
another_char_counts = {}

for char in another_string:
    if char in another_char_counts:
        another_char_counts[char] += 1
    else:
        another_char_counts[char] = 1

print(another_char_counts)
