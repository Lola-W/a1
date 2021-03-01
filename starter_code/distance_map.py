"""Assignment 1 - Distance map (Task 1)

CSC148, Winter 2021

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, Ian Berlott-Atwell, Jonathan Calver,
Sophia Huynh, Myriam Majedi, and Jaisie Sin.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Diane Horton, Ian Berlott-Atwell, Jonathan Calver,
Sophia Huynh, Myriam Majedi, and Jaisie Sin.

===== Module Description =====

This module contains the class DistanceMap, which is used to store
and look up distances between cities. This class does not read distances
from the map file. (All reading from files is done in module experiment.)
Instead, it provides public methods that can be called to store and look up
distances.
"""
from typing import Dict, Optional


class DistanceMap:
    """

    === Private Attributes ===
    _city1: str
    _city2: str
    _distance1: int
    _distance2: int
    _map: Dict[Tuple[str, str], int]

    """
    _city1: str
    _city2: str
    _distance: int
    _map: Dict[tuple[str, str], int]

    def __init__(self) -> None:
        self._map = {}

    def add_distance(self, city1: str, city2: str,
                     distance1: int, distance2: Optional[int] = None) -> None:
        """
        Adding distance to the _map
        """
        self._map[(city1, city2)] = distance1
        if isinstance(distance2, int):
            self._map[(city2, city1)] = distance2
        else:
            self._map[(city2, city1)] = distance1

    def distance(self, city1: str, city2: str) -> int:
        """
        Return the recorded distance, if not return -1.

        """

        if (city1, city2) in self._map:
            return self._map[(city1, city2)]
        else:
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
