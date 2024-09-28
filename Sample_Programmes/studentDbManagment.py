names:list = []
total:list = []
def input_names():
    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ")
        if name == "stop":
            break
        if name.strip() == "":
            print("Please Enter a Name")
        elif name not in names:
            names.append(name.strip())
        else:
            print(f"Name '{name}' is already in the list. Please enter a different name.")
input_names()
if names:
    idk:int = 1
    for x in names:
        total.append((idk, x))
        idk += 1
    print(f"\nComplete List of Students (Tuples):\n{total}\n\nList of Students with IDs:")
    for a in total:
        print(f"Id: {a[0]}, Name: {a[1]}")
    total_students:int = len(names)
    total_length:int = 0
    max_len:str = ""
    least_len:str = names[0]
    for x in names:
        total_length += len(x)
        if len(x) > len(max_len):
            max_len = x
        if len(x) <  len(least_len):
            least_len = x
    print(f"\nTotal number of students: {total_students}\nTotal length of all student names combined: {total_length}\nThe student with the longest name is: {max_len}\nThe student with the shortest name is: {least_len}")
else:
    print("No Name was Entered")