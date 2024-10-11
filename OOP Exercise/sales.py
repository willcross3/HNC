from car import Car

class Person:
    instance_count = 0
    def __init__(self, name, employee_id, total_sales):
        self.name = name
        self.employee_id = employee_id
        self.total_sales = total_sales
        Person.instance_count += 1
    def __str__(self):
        return f"{self.name} {self.employee_id} {self.total_sales}"
    def make_sale(self, car: Car):
        car.sell()
        self.total_sales += car.price
    def total_sales(self):
        return f"{self.name} has made a total of £{self.total_sales} in sales."

