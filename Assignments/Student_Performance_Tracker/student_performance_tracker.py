# Add students.
# Store their grades for different subjects.
# Calculate the student’s average score.
# Check if students are passing or failing based on a threshold.
# Calculate the class's average score.
# Display student performance in a structured manner.

from performance_tracker_functions import *

class student:
    
    total_stu:int = 0

    def __init__(self,name,math,science,english):
        self.name = name.lower().strip()
        self.math = math
        self.science = science
        self.english = english
        student.total_stu += 1   
    def average(self) -> float:
        return (self.math + self.english + self.science) / 3
    def status_check(self) -> list:
        fail = []
        if self.math < 40:
            fail.append("Mathematics")
        if self.science < 40:
            fail.append("Science")
        if self.english < 40:
            fail.append("English")
        return fail


def main():

    while True:
        print("===============================================\nWelcome to the Student Management System:")
        print("1. Add Student")
        print("2. Calculate Average Marks for a Specific Student")
        print("3. Calculate Average Marks for All Students")
        print("4. Check if a Specific Student is Pass or Fail")
        print("5. Check if All Students are Pass or Fail")
        print("6. Quit")

        choice = input("\nPlease select an option (1-6): ")

        if choice == '1':
            # Add student logic here
            pass
        elif choice == '2':
            # Calculate specific student's average marks
            pass
        elif choice == '3':
            # Calculate average marks for all students
            pass
        elif choice == '4':
            # Check if specific student passed
            pass
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
