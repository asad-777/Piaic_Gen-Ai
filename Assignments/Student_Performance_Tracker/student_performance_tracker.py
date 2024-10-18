class student:
    
    total_stu:int = 0
    s:list = []

    def __init__(self,name,math,science,english):
        self.name = name.lower().strip()
        self.math = math
        self.science = science
        self.english = english
        student.total_stu += 1   
    def average(self) -> float:
        return (self.math + self.english + self.science) / 3
    def status_check(self):
        fail = []
        if self.math < 40:
            fail.append("Mathematics")
        if self.science < 40:
            fail.append("Science")
        if self.english < 40:
            fail.append("English")
        if fail:
            return fail
        else:
            return None

class PerformanceTracker(student):
    @staticmethod
    def total_avg():
        if student.total_stu == 0:
                print("No Student Found!")
        else:
            total_avg = []
            for x in student.s:
                total_avg.append(x.average())
            for n in total_avg:
                sum = 0
                sum += n
            print(f"The total average score of all students is {sum/len(total_avg):.2f}")


def get_name():
    while True:
        name = input("Enter your name: ")
        for x in student.s:
            if x.name == name:
                print("Sorry that name already exists")
                break
        else:
            return name
            break     

def check_marks(mark):
    try:
        mark = int(mark)
        if mark >= 0 and mark <= 100:
            return mark
        else:   
            print("Please Enter Marks Between 0 and 100")
            return None
    except ValueError:
        print("Please Enter a valid number")
        return None
    
def get_grade():
    list = []
    while True:
        g1 = input("Enter Marks for Math: ")
        g1_c = check_marks(g1)
        if g1_c is not None: break
    while True:
        g2 = input("Enter Marks for Science: ")
        g2_c = check_marks(g2)
        if g2_c is not None: break
    while True:
        g3 = input("Enter Marks for English: ")
        g3_c = check_marks(g3)
        if g3_c is not None: break



    list.append(g1_c)
    list.append(g2_c)
    list.append(g3_c)
    return list

def add_student():
    name = get_name()
    grade = get_grade()

    new_obj = student(name,grade[0],grade[1],grade[2])
    student.s.append(new_obj)


def average_specific(name_1):
    for x in student.s:
        if x.name == name_1.lower().strip():
            return x.average()
        else:
            print("No student with that name exists")

def status_specific(name_1):
    for x in student.s:
        if x.name == name_1.lower().strip():
            return x.status_check()
        else:
            print("No student with that name exists")



def main():

    while True:
        print("\n===============================================\nWelcome to the Student Management System:")
        print("1. Add Student")
        print("2. Calculate Average Marks for a Specific Student")
        print("3. Calculate Average Marks for All Students")
        print("4. Check if a Specific Student is Pass or Fail")
        print("5. Check if All Students are Pass or Fail")
        print("6. Quit")
        choice = input("\nPlease select an option (1-6): ")
        if choice == '1':
            add_student() 
        elif choice == '2':
            name_for_average = input("\nEnter student's name for average: ")
            x = average_specific(name_for_average)
            print(f"{name_for_average}'s average score is {x:.2f}")
        elif choice == '3':
            PerformanceTracker.total_avg()
        elif choice == '4':
            name_for_status = input("\nEnter student's name: ")
            x = status_specific(name_for_status) 

            if x:
                print(f"Student is fail in {[i for i in x]}")
            else:
                print("Student is pass in all subjects")           
        elif choice == '5':
            # Check if all students passed
            pass
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()
