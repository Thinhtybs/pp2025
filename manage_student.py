class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.id} - {self.name} - {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
        self.marks = {}  # student_id : mark

    def __str__(self):
        return f"{self.id} - {self.name}"


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    # Input functions
    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"Student {i + 1}:")
            sid = input("ID: ")
            name = input("Name: ")
            dob = input("Date of Birth: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for i in range(n):
            print(f"Course {i + 1}:")
            cid = input("ID: ")
            name = input("Name: ")
            self.courses.append(Course(cid, name))

    def input_marks(self):
        self.list_courses()
        cid = input("Select course ID: ")

        course = next((c for c in self.courses if c.id == cid), None)
        if not course:
            print("Course not found")
            return

        for student in self.students:
            mark = float(input(f"Enter mark for {student.name}: "))
            course.marks[student.id] = mark

    # Listing functions
    def list_students(self):
        print("\nList of students:")
        for s in self.students:
            print(s)

    def list_courses(self):
        print("\nList of courses:")
        for c in self.courses:
            print(c)

    def show_marks_by_course(self):
        self.list_courses()
        cid = input("Enter course ID: ")

        course = next((c for c in self.courses if c.id == cid), None)
        if not course:
            print("Course not found")
            return

        print(f"\nMarks for course: {course.name}")
        for student in self.students:
            mark = course.marks.get(student.id, "N/A")
            print(f"{student.name}: {mark}")


def main():
    manager = StudentMarkManagement()

    while True:
        print("\n===== STUDENT MARK MANAGEMENT =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks by course")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            manager.input_students()
        elif choice == "2":
            manager.input_courses()
        elif choice == "3":
            manager.input_marks()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            manager.list_courses()
        elif choice == "6":
            manager.show_marks_by_course()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
