
class Car:
    def __init__(self, car_id, initial_location):
        self.id = car_id
        self.location = initial_location  # tuple (x, y)
        self.status = "available"  # Other states later
        self.destination = None  # Destination starts as None

    def __str__(self):
        return f"Car {self.id} at {self.location} - Status: {self.status}"
