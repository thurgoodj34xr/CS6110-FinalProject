from __future__ import annotations
from Intersection import Intersection
from Road import Road
from SimpleCar import SimpleCar


def __next_intersection(intersection: Intersection, road: Road) -> Intersection:
    """
    Find the next intersection from a given intersection, based on the road.
    This method assumes the road connects two intersections.
    """

    connecting_intersections = road.get_connecting_intersections()

    for inter in connecting_intersections:

        if inter != intersection:
            return inter

    raise RuntimeError("Failed to find intersection attached to road")


class Map:
    __slots__ = 'width', 'height', 'intersections', 'roads', 'cars'

    def __init__(self, **kwargs):
        self.intersections = []  # List of all intersections in the map
        self.roads = []  # List of all roads in the map
        self.cars = []
        if "intersections" in kwargs:
            self.intersections = kwargs["intersections"]
        if "roads" in kwargs:
            self.roads = kwargs["roads"]
        if "cars" in kwargs:
            self.cars = kwargs["cars"]
        if len(self.roads) == 0 or len(self.intersections) == 0 or len(self.cars) == 0:
            print("Creating default map")
            self.__create_default_map()

    def __create_default_map(self):
        intersection1 = Intersection()
        intersection2 = Intersection()
        intersection3 = Intersection()
        road1 = Road(speed_limit=50, intersections=[intersection1, intersection2])
        road2 = Road(speed_limit=60, intersections=[intersection2, intersection3])
        intersection1.add_road(road1, road2)
        intersection2.add_road(road1)
        intersection3.add_road(road2)
        self.cars = [SimpleCar(), SimpleCar(), SimpleCar(), SimpleCar(), SimpleCar()]
        self.intersections = [intersection1, intersection2, intersection3]
        self.roads = [road1, road2]

    def iterate(self):
        # Perform the iteration of the simulation (e.g., moving cars, updating state)
        print("Iterating simulation step.")

    def simulate(self):
        # Simulate the passage of time, car actions, etc.
        print("Simulating the environment.")

    def display_graph(self):

        # Display the map as a graph (perhaps using some graphical library)

        print("Displaying map graph.")
