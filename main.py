class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def describe(self):
        return f"Person ID: {self.person_id}, Name: {self.name}"


class Student(Person):
    # Student IS-A Person because a Student is a type of Person.
    # Inheritance allows Student to reuse Person's common data and behavior.
    def __init__(self, person_id, name, major):
        super().__init__(person_id, name)
        self.major = major

    def describe(self):
        return f"Student ID: {self.person_id}, Name: {self.name}, Major: {self.major}"


person = Person(100, "Ahmad")
student = Student(101, "Lina", "Computer Science")

print(person.describe())
print(student.describe())