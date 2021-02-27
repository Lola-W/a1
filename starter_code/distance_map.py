"""Assignment 1 - Distance map (Task 1)

CSC148, Winter 2021

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, Ian Berlott-Atwell, Jonathan Calver,
Sophia Huynh, Maryam Majedi, and Jaisie Sin.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Diane Horton, Ian Berlott-Atwell, Jonathan Calver,
Sophia Huynh, Maryam Majedi, and Jaisie Sin.

===== Module Description =====

This module contains the class DistanceMap, which is used to store
and look up distances between cities. This class does not read distances
from the map file. (All reading from files is done in module experiment.)
Instead, it provides public methods that can be called to store and look up
distances.
"""
from typing import Dict


class DistanceMap:
    """ A distance map that would store and give the distance for any
    two cities.

    ===== Private Attributes =====
    _distance_storage:
      The data structure as a dict with initial city A as a key and another dict
      as its value. The 'inner' dict stores the city A to any city B's distance.
    """

    _distance_storage: Dict[str, Dict[str, float]]

    def __init__(self):
        """Create a DistanceMap with empty _distance_storage.
        """
        self._distance_storage = {}

    def add_distance(self, city_a: str, city_b: str, distance: int) -> None:
        """Add distance to the _distance_storage attribute based on the input of
        city_a and city_a with their corresponding distance.

        >>> dm = DistanceMap()
        >>> dm.add_distance('a', 'b', 1)
        >>> dm.add_distance('a', 'c', 2)
        >>> dm.distance('a', 'b') == 1
        True
        >>> dm.distance('a', 'c') == 2
        True

        """

        if (city_a, city_b) not in self._distance_storage:
            raise NotImplementedError


    def distance(self, city_a: str, city_b: str) -> float:
        """Return the distance of city_a and city_b if the data is stored in the
        _distance_storage else -1.

        >>> dm = DistanceMap()
        >>> dm.add_distance('a', 'b', 1)
        >>> dm.distance('b', 'a') == -1
        True
        >>> dm.distance('c', 'a') == -1
        True
        >>> dm.distance('a', 'b') == 1
        True

        """
        if city_a in self._distance_storage:
            if city_b in self._distance_storage[city_a]:
                return self._distance_storage[city_a][city_b]
        return -1


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-import-modules': ['doctest', 'python_ta', 'typing'],
        'disable': ['E1136'],
        'max-attributes': 15,
    })
    import doctest

    doctest.testmod()
