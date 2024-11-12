from __future__ import annotations
from Car import Car
from Intersection import Intersection
from Road import Road


class AgentCar(Car):

    def __init__(self):
        super().__init__()

    def take_action(self, intersection: Intersection) -> Road:
        # Example: the agent might take the road with the highest current speed (adjusted by traffic)

        best_road = max(intersection.get_connecting_roads(), key=lambda road: road.get_speed())

        best_road.increment_traffic()  # Car chooses this road, so we increment traffic

        return best_road

    def learn(self, roads: list[Road]):
        # An agent could learn based on past actions or traffic conditions

        print("Agent learning from roads:", roads)
