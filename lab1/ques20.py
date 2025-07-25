print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice(1/2/3/4): ")

num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

num1 = float(num1_str)
num2 = float(num2_str)

if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid input. Please enter a valid choice (1/2/3/4).")

