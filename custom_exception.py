# Define a custom exception
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Must be 18 or older.")

# Function that uses the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is valid for access.")

# Example usage with exception handling
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid number.")
