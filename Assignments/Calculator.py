def fn_add(a: int, b: int):
    return a + b


def fn_sub(a: int, b: int):
    return a - b


def fn_mul(a: int, b: int):
    return a * b


def fn_div(a: int, b: int):
    if b == 0:
        return "Error: Division by Zero"
    else:
        return a / b


# Function to get valid integer input or quit
def get_input(prompt):
    while True:
        val = input(prompt)
        if val.lower() == "q":
            return None
        try:
            return int(val)
        except ValueError:
            print("Invalid input. Please enter an integer or 'q' to quit.")


# Main loop
while True:
    val1 = get_input("Enter first value or 'q' to quit: ")
    if val1 is None:  # User wants to quit
        break

    val2 = get_input("Enter second value: ")
    if val2 is None:  # Handle quitting here too
        break

    print("Choose Operation:")
    print("For Addition: +")
    print("For Subtraction: -")
    print("For Multiplication: * or x")
    print("For Division: /")

    # Map operators to functions
    operations = {
        "+": fn_add,
        "-": fn_sub,
        "*": fn_mul,
        "x": fn_mul,
        "/": fn_div
    }

    op = input("Enter operation: ").strip().lower()

    if op in operations:
        result = operations[op](val1, val2)
        print(f"Result: {result}")
    else:
        print("Invalid operation. Please choose a valid operator.")

    print()  # Print a newline for better readability
