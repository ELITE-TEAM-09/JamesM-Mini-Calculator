while True:
    try:
        num1 = float(input("Enter First Number:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    op = input("Enter Operator:")
    if op in ['+', '-', '*', '/']:
        break
    else:
        print("Invalid operator. Please enter '+', '-', '*', or '/'.")

while True:
    try:
        num2 = float(input("Enter Second Number:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Division by zero is not allowed.")
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator!")
