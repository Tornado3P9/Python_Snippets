from typing import List, Tuple

# Define a type alias
Coordinates = List[Tuple[float, float]]

def get_coordinates() -> Coordinates:
    return [(1.0, 2.0), (3.0, 4.0)]

# Usage
coords: Coordinates = get_coordinates()

print(type(coords))
