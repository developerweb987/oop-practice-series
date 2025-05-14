class Bank:
    # Class variable
    bank_name = "Global Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_bank_name(self):
        print(f"Bank Name: {Bank.bank_name}")

# Create instances
customer1 = Bank()
customer2 = Bank()

# Display original bank name
customer1.display_bank_name()
customer2.display_bank_name()

# Change bank name using class method
Bank.change_bank_name("Future Finance")

# Display updated bank name for all instances
customer1.display_bank_name()
customer2.display_bank_name()
