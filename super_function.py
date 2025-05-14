# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called. Name: {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the base class constructor
        self.subject = subject
        print(f"Teacher constructor called. Subject: {self.subject}")

# Example usage
teacher1 = Teacher("Mr. Smith", "Physics")
