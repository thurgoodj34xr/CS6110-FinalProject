from __future__ import annotations


class Intersection:
    __slots__ = '__connecting_roads'

    def __init__(self):
        self.__connecting_roads = []  # List of roads connected to this intersection

    def add_road(self, *roads: Road):
        for road in roads:
            self.__connecting_roads.append(road)

    def get_connecting_roads(self) -> list[Road]:
        return self.__connecting_roads
