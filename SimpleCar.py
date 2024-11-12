from __future__ import annotations
from Car import Car
from Intersection import Intersection
from Road import Road


class SimpleCar(Car):

    def __init__(self):
        super().__init__()

    def take_action(self, intersection: Intersection) -> Road:
        # Example: simple car randomly selects a road

        import random

        road = random.choice(intersection.get_connecting_roads())

        road.increment_traffic()  # Car chooses this road, so we increment traffic

        return road

    def learn(self, roads: list[Road]):
        # SimpleCar doesn't learn, it just takes random actions

        pass

    def is_satisfied(self) -> bool:
        # SimpleCar might be satisfied after a fixed number of steps or upon reaching a goal

        return False  # Example assumption
