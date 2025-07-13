from car import Car
from rider import Rider
from simulation import Simulation

car1 = Car("CAR001", (10, 5))
rider1 = Rider("RIDER_A", (1, 2), (20, 15))
sim = Simulation()
sim.cars[car1.id] = car1
sim.riders[rider1.id] = rider1

print(car1)
print(rider1)
print(sim)

