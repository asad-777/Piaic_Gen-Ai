def get_input(prompt):
    while True:
        val = input(prompt)
        if val.lower() == 'q':
            return None
        try:
            return int(val)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
while True:
    val1 = get_input("Enter First Value or 'q' to Quit: ")
    if val1 == None:break
    val2 = get_input("Enter Second Value: ")
    if val2 == None:break
    operators = {
        "+" : lambda val1,val2 : val1 + val2,
        "-" : lambda val1,val2 : val1 - val2,
        "*" : lambda val1,val2 : val1 * val2,
        "x" : lambda val1,val2 : val1 * val2,
        "/" : lambda val1,val2 : val1 / val2 if val2 != 0 else "Division by zero is not allowed"
    }
    while True:        
        print("\nSelect an Operation:\n\nAddition: +\nSubtraction: -\nMultiplication: x or *\nDivision: /")
        op = input("Enter Operator: ")
        if op in operators:
            print(f"{val1} {op} {val2} = {operators[op](val1, val2)}\n")
            break
        else:
            print("\nOperator not found! please enter valid operator")