from __future__ import annotations
from abc import ABC, abstractmethod
from Intersection import Intersection
from Road import Road
import math

class Car(ABC):
    __slots__ = 'road_memory'

    def __init__(self):
        self.road_memory: dict[Road, float] = {}

    @abstractmethod
    def take_action(self, intersection: Intersection) -> Road:
        """
        The car takes action based on its current state and the available roads at the intersection.
        Returns a road to travel to the next intersection.
        """
        pass

    @abstractmethod
    def learn(self, roads: list[Road]):
        """
        The car learns about available roads, possibly improving decision-making in the future.
        """
        for road in roads:
            if road in self.road_memory:
                self.road_memory[road] = (self.road_memory[road] + road.get_speed()) / 2
            else:
                self.road_memory[road] = road.get_speed()
