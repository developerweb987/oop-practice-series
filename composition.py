# Engine class
class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine

    def start(self):
        return f"The {self.type_of_engine} engine is starting."

# Car class using composition
class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Engine object passed during initialization

    def start_car(self):
        return f"{self.model}: {self.engine.start()}"

# Example usage
engine1 = Engine("V8")
car1 = Car("Ford Mustang", engine1)

# Accessing Engine method via Car class
print(car1.start_car())
