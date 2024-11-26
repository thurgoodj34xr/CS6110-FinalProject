from __future__ import annotations
from Map import Map

if __name__ == "__main__":
    my_map = Map()

    start = my_map.intersections[0]
    end = my_map.intersections[-1]

    shortest_path = my_map.find_shortest_path(start, end)
    print("Shortest Path:", shortest_path)

    cheapest_path = my_map.find_cheapest_path(start, end)
    print("Cheapest Path:", cheapest_path)

    shortest_time_path = my_map.find_shortest_time_path(start, end)
    print("Shortest Time Path:", shortest_time_path)

    highest_speed_path = my_map.find_highest_speed_limit_path(start, end)
    print("Path with Highest Speed Limit:", highest_speed_path)
