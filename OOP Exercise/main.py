import car
import sales

car_data = {
    "car0": car.Car("Ford", "F150", 2024, 50000, True, True),
    "car1": car.Car("Toyota", "Corolla", 2022, 25000, False, True),
    "car2": car.Car("Ford", "Mustang", 2023, 30000, False, False),
    "car3": car.Car("Chevy", "Camaro", 2024, 35000, True, True),
    "car4": car.Car("Porsche", "911", 2022, 100000, False, True)
}

sales_data = {
    "sales0": sales.Person("George", 1000, 0),
    "sales1": sales.Person("John", 2000, 0),
    "sales2": sales.Person("Sarah", 3000, 0),
    "sales3": sales.Person("Emily", 4000, 0),
    "sales4": sales.Person("Michael", 5000, 0)    
}

def add_new_car():
        name = input("Enter the name of the car: ")
        make = input("Enter the make of the car: ")
        model = input("Enter the model of the car: ")
        year = int(input("Enter the year of the car: "))
        price = float(input("Enter the price of the car: "))
        is_new = input("Is the car new? ").lower()
        if is_new == "yes":
            is_new = True
        else:
            is_new = False
        new_car = car.Car(make, model, year, price, is_new, in_stock=True)
        car_data[name] = new_car
        print(f"{name} has been added to the catalogue.")


def get_cars():
    for car in car_data.values():
        print(car.make, car.model, car.year)

def get_sales():
    for sales in sales_data.values():
        print(sales.name, sales.employee_id, sales.total_sales)


get_sales()


""" get_cars()
add_new_car()
get_cars() """