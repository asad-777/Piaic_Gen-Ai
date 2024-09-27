import random

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    print(f"Your Number is {y}, guess if Computer has a greater number or a lower number ?")
    guess:int = input_user("Choose an Option:  ")