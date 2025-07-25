number_to_check = 29
is_prime = True

if number_to_check <= 1:
    is_prime = False
else:
    i = 2
    while i * i <= number_to_check:
        if number_to_check % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")

number_to_check_2 = 30
is_prime_2 = True

if number_to_check_2 <= 1:
    is_prime_2 = False
else:
    i = 2
    while i * i <= number_to_check_2:
        if number_to_check_2 % i == 0:
            is_prime_2 = False
            break
        i += 1

if is_prime_2:
    print(f"{number_to_check_2} is a prime number.")
else:
    print(f"{number_to_check_2} is not a prime number.")
