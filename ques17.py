n_terms_str = input("Enter the number of terms for Fibonacci sequence: ")
n_terms = int(n_terms_str)

first_term = 0
second_term = 1

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to 1 term:")
    print(first_term)
else:
    print(f"Fibonacci sequence up to {n_terms} terms:")
    print(first_term)
    print(second_term)
    count = 2
    while count < n_terms:
        next_term = first_term + second_term
        print(next_term)
        first_term = second_term
        second_term = next_term
        count += 1
