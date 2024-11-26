from __future__ import annotations


class Road:

    def __init__(self, speed_limit: int, intersections: list[Intersection], length:float):
        self.speed_limit = speed_limit  # The base speed limit set at construction time
        self.intersections = intersections  # List of intersections this road connects
        self.traffic_count = 0  # Track the number of cars using this road
        self.length = length

    def get_speed(self) -> float:
        # Adjust the speed limit based on traffic count
        # For simplicity, we'll reduce the speed by 5 for each car using the road
        # but not allowing the speed to go below a minimum value
        congestion_factor = 5  # The reduction in speed per car
        min_speed = 10  # Minimum speed limit (no matter how many cars)
        adjusted_speed = max(self.speed_limit - self.traffic_count * congestion_factor, min_speed)
        return adjusted_speed

    def get_connecting_intersections(self) -> list[Intersection]:
        return self.intersections

    def increment_traffic(self):
        self.traffic_count += 1

    def decrement_traffic(self):
        if self.traffic_count > 0:
            self.traffic_count -= 1
    
    def get_cost(self) -> float:
        base_cost = 1.0  # Assume a base cost per kilometer
        traffic_cost = 0.5 * self.traffic_count  # Extra cost per car
        return self.length * base_cost + traffic_cost