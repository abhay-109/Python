prime_numbers_set = set()
for num in range(2, 50):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers_set.add(num)

print(f"Prime numbers less than 50: {prime_numbers_set}")

given_number = 23
if given_number in prime_numbers_set:
    print(f"The number {given_number} exists in the set of prime numbers.")
else:
    print(f"The number {given_number} does not exist in the set of prime numbers.")

given_number_2 = 51
if given_number_2 in prime_numbers_set:
    print(f"The number {given_number_2} exists in the set of prime numbers.")
else:
    print(f"The number {given_number_2} does not exist in the set of prime numbers.")
