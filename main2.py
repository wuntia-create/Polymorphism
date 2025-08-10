class MobilePhone:
    def __init__(self, model, max_price):
        self.model = model
        self.__max_price = max_price
    def sell(self):
        print(f"Selling {self.model} for ${self.__max_price}")
    def set_max_price(self, new_price):
        self.__max_price = new_price
phone = MobilePhone("Samsung Galaxy S25", 1200)
phone.sell()
phone.__max_price = 800
phone.sell()
new_price = float(input("Enter the new selling price: "))
phone.set_max_price(new_price)
phone.sell()