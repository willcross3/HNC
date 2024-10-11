from datetime import datetime
import sales

class Car:
    instance_count = 0
    def __init__(self, make, model, year, price, is_new, in_stock):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.is_new = is_new
        self.in_stock = in_stock
        Car.instance_count += 1
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.price} {self.is_new}"
    def sell(self):
        if self.in_stock == False:
            print(f"{self.make} {self.model} is out of stock.")
        else:
            print(f"{self.make} {self.model} has been sold for £{self.price}")
            self.in_stock = False
            current_datetime = datetime.now()
            self.date_of_sale = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
    def inventory(self):
        if self.in_stock == True:
            return f"{self.make} {self.model} {self.year} is in stock."
        else:
            return f"{self.make} {self.model} {self.year} is not in stock."
    






