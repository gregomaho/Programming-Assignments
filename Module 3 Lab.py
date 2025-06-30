#Author: Gregory Mahoy
#Course: SDEV220
#Date: 06/30/25
#Description: This program defines a Vehicle class and an Automobile subclass.
# It collects information about a car and prints it out.
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    vehicle_type = "car"
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")

    doors = ""
    while doors not in ["2", "4"]:
        doors = input("Number of doors (2 or 4): ")

    roof = ""
    while roof not in ["solid", "sun roof"]:
        roof = input("Type of roof (solid or sun roof): ").lower()

    car = Automobile(vehicle_type, year, make, model, int(doors), roof)

    print("\nVehicle Information:")
    print("Vehicle type:", car.vehicle_type)
    print("Year:", car.year)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Number of doors:", car.doors)
    print("Type of roof:", car.roof)

if __name__ == "__main__":
    main()
