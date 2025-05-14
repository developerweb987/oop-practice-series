class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self  # Returns the iterator object (self)

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stops iteration when below 0
        value = self.current
        self.current -= 1
        return value

# Example usage
cd = Countdown(5)

for number in cd:
    print(number)
