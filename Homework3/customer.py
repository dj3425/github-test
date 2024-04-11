# creating class and setting variables/parameters
class Customer:
    _accountNumber = 0
    _amount = 0

# creating an initializer value that initializes every value created to include a parameter
    def __init__(self, accountNumber, amount):
        self._accountNumber = accountNumber
        self._amount = amount

# create method for increasing amount with interest payment amt
    def calculateInterestPayment(self):
        self._amount *= 1.05

    @property
    def accountNumber(self):
        return self._accountNumber
