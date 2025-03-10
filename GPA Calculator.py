import math


def calculate_gpa(num_courses, marks):
    """
    Calculate GPA for semester based on given number of courses and entering marks.

    Args:
        num_courses(int): Number of courses
        marks(int): If 0, enter total marks, if 1, enter marks to Mid Sem, Internals, and End Sem.

    Return:
        Calculated GPA for the semester (float)
    """
    credits = 0
    total_credits = 0

    for i in range(num_courses):
        course_name = input("Enter Course Name: ")
        course_credits = int(input(f"Enter Total Credits Of {course_name}: "))
        if marks == 0:
            course_marks = int(input(f"Enter Total Marks Acquired for {course_name}: "))
        else:
            mid_sem_marks = int(input(f"Enter Your Mid Sem Marks for {course_name}: "))
            internal_marks = int(
                input(f"Enter Your Internal Marks for {course_name}: ")
            )
            end_sem_marks = int(input(f"Enter Your End Sem Marks for {course_name}: "))
            course_marks = mid_sem_marks + internal_marks + end_sem_marks

        print()
        if course_marks > 100:
            print("Enter Valid Marks")
            credits = 0
            total_credits = 1
            break
        elif course_marks < 100:
            course_marks += 1 
        course_point = math.ceil(course_marks / 10)

        credits += course_point * course_credits
        total_credits += course_credits

    gpa = credits / total_credits
    return gpa


if __name__ == "__main__":
    print("\n------------------------------------------")
    print("GPA Calculator: ")
    print("------------------------------------------")

    num_courses = int(input("Enter Number Of Courses: "))
    marks = int(
        input(
            "Enter 1 to individually enter Mid Sem, Internals & End Sem Marks\nElse Enter 0 to enter Total Marks: "
        )
    )

    gpa = calculate_gpa(num_courses, marks)
    print("Your Credits for this Semester is:", gpa)