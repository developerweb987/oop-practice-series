class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    # Instance method
    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof! Woof!")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()
