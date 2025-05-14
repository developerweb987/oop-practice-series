class Logger:
    def __init__(self):
        print("Logger initialized. Object created.")

    def __del__(self):
        print("Logger shutting down. Object destroyed.")

# Example usage
log = Logger()

# Optionally delete the object manually
del log

# Or let it be destroyed automatically when the script ends
