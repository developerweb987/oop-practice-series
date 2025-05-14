class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):
    pass

# Example usage
d = D()
d.show()

# Print the MRO
print("Method Resolution Order (MRO):")
print([cls.__name__ for cls in D.__mro__])
