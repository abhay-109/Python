number_str = input("Enter a number to check if it's a palindrome: ")

reversed_number_str = number_str[::-1]

if number_str == reversed_number_str:
    print(f"The number {number_str} is a palindrome.")
else:
    print(f"The number {number_str} is not a palindrome.")

# Example with another number
test_number_str = "12321"
reversed_test_number_str = test_number_str[::-1]

if test_number_str == reversed_test_number_str:
    print(f"The number {test_number_str} is a palindrome.")
else:
    print(f"The number {test_number_str} is not a palindrome.")

# Example with a non-palindrome
another_test_number_str = "12345"
reversed_another_test_number_str = another_test_number_str[::-1]

if another_test_number_str == reversed_another_test_number_str:
    print(f"The number {another_test_number_str} is a palindrome.")
else:
    print(f"The number {another_test_number_str} is not a palindrome.")
