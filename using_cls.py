class Counter:
    # Class variable to keep track of object count
    count = 0

    def __init__(self):
        # Each time an object is created, increment the count
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Display the count using cls
        print(f"Total objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the number of objects created
Counter.display_count()
