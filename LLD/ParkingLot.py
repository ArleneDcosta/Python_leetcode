from enum import Enum

class VehicleType(Enum):
    CAR = 2  
    BIKE = 1  
    TRUCK = 3

class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self, spot_id, spot_size, hourly_rate):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.hourly_rate = hourly_rate  
        self.is_available = True
        self.vehicle = None
        self.parked_hours = 0  

    def park_vehicle(self, vehicle, hours=1):
        if self.is_available and self.spot_size >= vehicle.vehicle_type.value:
            self.vehicle = vehicle
            self.is_available = False
            self.parked_hours = hours
            return True
        return False

    def remove_vehicle(self):
        if self.vehicle:
            fee = self.calculate_fee()
            print(f"Vehicle {self.vehicle.license_plate} removed from spot {self.spot_id}. Parking fee: ${fee:.2f}")
            self.vehicle = None
            self.is_available = True
            self.parked_hours = 0
            return fee
        return 0

    def calculate_fee(self):
        return self.parked_hours * self.hourly_rate

class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_parking_spot(self, spot):
        self.spots.append(spot)

    def find_spot_for_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.park_vehicle(vehicle, hours):
                return spot
        return None


def main():
    # Create a parking lot
    parking_lot = ParkingLot()

    # Add parking spots with different rates
    parking_lot.add_parking_spot(ParkingSpot(2, VehicleType.CAR.value, hourly_rate=5.0))
    parking_lot.add_parking_spot(ParkingSpot(1, VehicleType.BIKE.value, hourly_rate=2.0))
    parking_lot.add_parking_spot(ParkingSpot(3, VehicleType.TRUCK.value, hourly_rate=8.0))

    # Create vehicles
    car = Vehicle("CAR-123", VehicleType.CAR)
    bike = Vehicle("BIKE-456", VehicleType.BIKE)
    truck = Vehicle("TRUCK-789", VehicleType.TRUCK)

    # Try parking the vehicles for different durations
    car_spot = parking_lot.find_spot_for_vehicle(car, hours=3)  # Parked for 3 hours
    if car_spot:
        print(f"Car parked at spot {car_spot.spot_id} for 3 hours.")
    else:
        print("No parking spot available for the car.")

    bike_spot = parking_lot.find_spot_for_vehicle(bike, hours=2)  # Parked for 2 hours
    if bike_spot:
        print(f"Bike parked at spot {bike_spot.spot_id} for 2 hours.")
    else:
        print("No parking spot available for the bike.")

    truck_spot = parking_lot.find_spot_for_vehicle(truck, hours=4)  # Parked for 4 hours
    if truck_spot:
        print(f"Truck parked at spot {truck_spot.spot_id} for 4 hours.")
    else:
        print("No parking spot available for the truck.")

    # Remove a vehicle and calculate the fee
    if car_spot:
        car_spot.remove_vehicle()

    if bike_spot:
        bike_spot.remove_vehicle()

    if truck_spot:
        truck_spot.remove_vehicle()

if __name__ == "__main__":
    main()
