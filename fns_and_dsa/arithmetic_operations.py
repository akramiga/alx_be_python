def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide" and num2 or num1 == 0:
        print("Cannot divide by zero!!!!")
    else:
        return num1 / num2    