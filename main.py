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


person = Person(100, "Ahmad")
student = Student(101, "Lina", "Computer Science")

print(person.describe())
print(student.describe())


print(student)

course1 = Course("CS101", "Introduction to Programming", 2)
course2 = Course("DB101", "Introduction to Databases", 3)

print(course1)
print(course2)