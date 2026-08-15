class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def describe(self):
        return f"Person ID: {self.person_id}, Name: {self.name}"


class Student(Person):
    def __init__(self, person_id, name, major):
        super().__init__(person_id, name)
        self.major = major

    def describe(self):
        return f"Student ID: {self.person_id}, Name: {self.name}, Major: {self.major}"

    def __str__(self):
        return f"Student ID: {self.person_id}, Name: {self.name}, Major: {self.major}"


class Course:
    def __init__(self, code, name, seats):
        self.code = code
        self.name = name
        self.seats = seats

    def __str__(self):
        return f"Course: {self.code} - {self.name} - Seats: {self.seats}"


class Enrollment:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if value < 0 or value > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.__grade = value


class Registry:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student, course, grade):
        enrollment = Enrollment(student, course, grade)
        self.enrollments.append(enrollment)

    def show_students(self):
        print("\n--- Students ---")
        for student in self.students:
            print(student)

    def show_courses(self):
        print("\n--- Courses ---")
        for course in self.courses:
            print(course)

    def show_enrollments(self):
        print("\n--- Enrollments ---")
        for enrollment in self.enrollments:
            print(
                f"{enrollment.student.name} -> "
                f"{enrollment.course.code} -> "
                f"Grade: {enrollment.grade}"
            )

            
# 1 tests
person = Person(100, "Ahmad")
student = Student(101, "Lina", "Computer Science")

print(person.describe())
print(student.describe())

#  2 test
print(student)


# 3 tests
course1 = Course("CS101", "Introduction to Programming", 2)
course2 = Course("DB101", "Introduction to Databases", 3)
print(course1)
print(course2)


# 4 & 5 test
enrollment = Enrollment(student, course1, 85)
print(enrollment.student.name)
print(enrollment.course.code)
print(enrollment.grade)

#6 test
registry = Registry()
registry.add_student(person)
registry.add_student(student)
registry.add_course(course1)
registry.add_course(course2)
registry.enroll_student(student, course1, 85)
registry.show_students()
registry.show_courses()
registry.show_enrollments()

# Part 7 - Error Handling

registry = Registry()

registry.add_student(person)
registry.add_student(student)

registry.add_course(course1)
registry.add_course(course2)

try:
    grade_input = input("Enter grade: ")
    grade = int(grade_input)

    registry.enroll_student(student, course1, grade)

    print("Grade accepted and enrollment created.")

except ValueError as error:
    print(f"Error: {error}")