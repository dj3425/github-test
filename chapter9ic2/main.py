class Automobile:
    weight = 0
    mileage = 0
    price = 0
    model = ''
    def __init__(self, model, price):
        self.model = model
        self.price = price
    def calculatePrice(self):
        if self.mileage > 200000:
            self.price = 10000
        else:
            self.price = 40000

    def __str__(self):
        return "This car weighs %d and has mileage of %d and a price of %d" % (self.weight,self.mileage,self.price)
    def driveCar100000Miles(self):
        self.mileage = self.mileage + 100000
        self.calculatePrice()

bronco = Automobile('blackDiamond',57000)
print(bronco)
bronco.driveCar100000Miles()
print(bronco)
bronco.driveCar100000Miles()
bronco.driveCar100000Miles()
print(bronco)
civic = Automobile('Sport', 25000)
print(civic)
bronco.weight = 19
print(bronco.weight)
print(bronco.price)
