class Simulation:
    def __init__(self):
        self.cars = {}
        self.riders = {}

    def __str__(self):
        return (f"Simulation with {len(self.cars)} cars "
                f"and {len(self.riders)} riders.")
