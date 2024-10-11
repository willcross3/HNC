import datetime
from PIL import Image
from dateutil.relativedelta import relativedelta

print("Welcome to Rent a Car")
car = ""
# Input for DOB
Year = int(input("Please enter your year of birth > "))
Month = int(input("Please enter your month of birth > "))
Day = int(input("Please enter your date of birth > "))

# Calculating age
DOB = datetime.datetime(Year, Month, Day)
Age = relativedelta(datetime.datetime.now(), DOB)

if Age.years < 24:
    print("We are sorry but you are not old enough to rent a car from us")
    raise SystemExit(0)
else:
    print("Please continue")

# Input for Name, Nationality, and Lengthoflicence
while True:
    name = input("Please enter your first and last name > ")
    if not name:
        print("Please enter a valid name.")
        continue
    break

while True:
    nationality = input("Please enter your nationality > ")
    if not nationality:
        print("Please enter a valid nationality.")
        continue
    break

while True:
    LengthOfLicense = input("Please enter how long you have held your licence in years > ")
    if not LengthOfLicense.isdigit() or int(LengthOfLicense) <= 0:
        print("Please enter a valid number of years.")
        continue
    LengthOfLicense = int(LengthOfLicense)
    break

# Giving cars images
try:
    SmallCar = Image.open(r"small_car.jpg")
    MediumCar = Image.open(r"medium_car.jpg")
    LargeCar = Image.open(r"large_car.jpg")
except FileNotFoundError:
    print("One or more car images are missing. Please check the file paths.")
    raise SystemExit(1)

# Input for Car and rental time
while True:
    car = input("Please enter the car that you want to rent: Small, Medium, or Large >")
    if car.upper() == "SMALL":
        SmallCar.show()
    elif car.upper() == "MEDIUM":
        MediumCar.show()
    elif car.upper() == "LARGE":
        LargeCar.show()
    else:
        print("Invalid car choice. Please choose Small, Medium, or Large.")
        continue

    IsUserSure = input("Do you want to continue? (Yes/No) > ")
    if IsUserSure.lower() == "no":
        continue
    elif IsUserSure.lower() == "yes":
        pass

    RentalTime = int(input("Please enter how many days you want to rent this vehicle > "))

    # Calculating rental time
    RentalMonths = RentalTime // 30
    RentalWeeks = (RentalTime - RentalMonths * 30) // 7
    RentalDays = (RentalTime - RentalMonths * 30 - RentalWeeks * 7)

    # Displaying the results
    cost = (RentalMonths * 270) + (RentalWeeks * 95) + (RentalDays * 30)
    vat = cost * 0.20
    total_cost = cost + vat

    print(f"You will be renting a {car} car for {RentalMonths} Months, {RentalWeeks} Weeks, and {RentalDays} Days")
    print(f"This will cost £{total_cost:.2f} (including VAT of £{vat:.2f})")
    
    break
