import pandas as pd
import os  
class Students:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english  
    @classmethod
    def save_to_csv(cls, name, math, science, english, filename="students.csv"):
        df = pd.DataFrame({
            "Names": [name],
            "Math": [math],
            "Science": [science],
            "English": [english],
        })
        if os.path.isfile(filename) and os.path.getsize(filename)>0:
            df.to_csv(filename, mode='a', header=False, index=False)
        else:
            df.to_csv(filename, mode='w', header=True, index=False)
def check_df():
    if os.path.isfile("students.csv") and os.path.getsize("students.csv") > 0:
        df = pd.read_csv("students.csv")
        return df
    else:
        return None   
def name_unique(x):
    y = check_df()
    if y is not None:
        if x in y["Names"].values:
            return False
        else:
            return True
    else:
        return True
def get_info():
    print()
    while True:
        name = input("Enter Name of Student: ")
        if name.isalpha():
            name = name.lower().strip()
            if name_unique(name):
                break
            else:
                print("Name Already exists, Please enter a Unique Name !")
                continue
        else:
            print("Please Enter a Valid Name!")
            continue
    grades = []
    def get_grades(subject) -> int:
        while True:
            x = input(f"Enter Grades in {subject}: ")
            try:
                x = int(x)
                if 0 <= x <= 100:
                    return x
                else:
                    print("Please Enter a value between 0 and 100!")
                    continue
            except ValueError:
                print("Please Enter a Valid Grade!")
                continue
    grades.append(get_grades("Math"))
    grades.append(get_grades("Science"))
    grades.append(get_grades("English"))
    new_student = Students(name, grades[0], grades[1], grades[2])
    Students.save_to_csv(new_student.name, new_student.math, new_student.science, new_student.english)
def main():
    print("Welcome to Lms\n==================================================\n")
    while True:
        print()
        print("Press 1 to add Student")
        print("Press 2 to check all available students")
        print("Press 3 to Check Average for a specific Student")
        print("Press 4 to Calculate Average Marks for all class")
        print("Press 5 to Check Pass / Fail status of specific Student")
        print("Press 6 to check Pass/Fail status of Complete class")
        print("Press 7 to Quit")
        x = input("\nEnter Your Choice Here: ")
        if x == "1":
            get_info()
            print("==================================================")
        elif x == "2":
            y = check_df()
            if y is not None:
                print("\n==================================================")
                print(y.to_string())
                print("==================================================")
            else:
                print("No Student found ! ")
                continue
        elif x == "3":
            name_avg = input("Enter students name: ").lower().strip()
            y = check_df()
            if y is not None:
                h = True
                for index,value in y.iterrows():
                    if name_avg == value["Names"]:
                        avg:float =  (value["Math"] + value["Science"] + value["English"]) / 3.0
                        print(f"The Average Marks of {value["Names"]} is {avg:.2f}")
                        print("==================================================")
                    else:
                        h = None
                if h is None:
                    print("No Such name was Found !")
                    print("==================================================")              
            else:
                print("No students found !")
                print("==================================================")
        elif x == "4":
            y = check_df()
            if y is not None:
                sum = 0
                for a,values in y.iterrows():
                    sum += (values["Math"] + values["Science"] + values["English"])
                avg = sum /  (len(y)*3.0)
                print(f"The average score of complete class is {avg:.2f}")
                print("==================================================")
            else:
                print("No Students were found !")
                print("==================================================")
        elif x == "5":
            y = check_df()
            if y is not None:
                name_pf = input("Enter Name of Student: ").lower().strip()
                found = False  
                for index, value in y.iterrows():
                    if name_pf == value["Names"]:
                        found = True
                        fail_subj = []
                        if value["English"] < 40:
                            fail_subj.append("English")
                        if value["Math"] < 40:
                            fail_subj.append("Math")
                        if value["Science"] < 40:
                            fail_subj.append("Science")
                        if fail_subj:
                            print(f"{name_pf} has failed in: {', '.join(fail_subj)}")
                        else:
                            print(f"{name_pf} has passed all subjects.")
                        break  
                if not found:
                    print("No Such Student was found!")
                print("==================================================")
            else:
                print("No Students were found!")
                print("==================================================")
        elif x == "6":
            y = check_df()
            if y is not None:
                sum = 0
                for a,values in y.iterrows():
                    sum += (values["Math"] + values["Science"] + values["English"])
                avg = sum /  (len(y)*3.0)
                if avg < 40:
                    print("The Class failed !")
                else:
                    print("Total Class Passed !")
        elif x == "7":
            print("Good Bye!")
            break
        else:
            print("Please Enter a Valid Choice!")
            print("==================================================")
if __name__ == "__main__":
    main()