class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an instance of Multiplier
times3 = Multiplier(3)

# Check if the object is callable
print("Is times3 callable?", callable(times3))

# Use the object like a function
result = times3(10)
print("Result of times3(10):", result)
