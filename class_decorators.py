# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # Add the method to the class
    return cls

# Apply the decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Alice")
print(p.greet())  # Using the method added by the decorator
