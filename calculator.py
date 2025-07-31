first_digit = float(input("What's the first number that comes to your mind? "))
second_digit = float(input("What's the second number? "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = first_digit + second_digit
elif operation == "-":
    result = first_digit - second_digit
elif operation == "*":
    result = first_digit * second_digit
elif operation == "/":
    if second_digit != 0:
        result = first_digit / second_digit
    else:
        result = None
        print(f"{first_digit} cannot divide by 0")
else:
    print("Invalid operation selected.")
    result = None

if result is not None:
    print(f"{first_digit} {operation} {second_digit} = {result}")
