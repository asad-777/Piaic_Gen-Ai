import random
def input_user(prompt:str):
    valid_inputs:list = ["higher", "lower"]
    while True:
        user_input = input(prompt)
        user_input = user_input.lower()
        if user_input in valid_inputs:
            if user_input == valid_inputs[0]:
                return True 
            else:   
                return False
        else:
            print("Enter a Valid Input i.e 'higher' or 'lower'")
print("Welcome to the High-Low Game!\n---------------------------------")
round:int = 1
max_round:int = 3
score:int = 0
while round <= max_round:
    x: int = random.randint(1, 100)
    y: int = random.randint(1, 100)
    while x == y:
        y = random.randint(1,100)
    print(f"Round {round}:")
    print(f"Your Number is {x}")
    # true is greater and false is lesser
    ui:bool = input_user("Do you think your number is higher or lower than the computer's?")
    if (x > y and ui) or (x < y and not ui):
        print(f"You were right! The computer's number was {y}")
        score += 1
        print(f"Your score is now {score}")
    else:
        print(f"You were wrong! The computer's number was {y}")
        print(f"Your score is now {score}")
    print()
    round += 1