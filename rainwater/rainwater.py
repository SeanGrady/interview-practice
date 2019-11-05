from typing import List
from collections import defaultdict


def trap(heightmap: List[int]) -> int:
    """
    This takes the heightmap and breaks it down into a series of lists, one
    for each 'elevation'. Since there is only water trapped if it is between
    two 'rocks', you can just look for any gaps between two 'rocks' at each
    elevation to get the total water at each elevation, then sum to get the
    total water in the 'map'
    """
    # add class/self for testing on leetcode
    topo_lines = defaultdict(list)
    total_water = 0
    for index, top_height in enumerate(heightmap):
        height = top_height
        while height > 0:
            topo_lines[height].append(index)
            height -= 1

    for height, indexes in topo_lines.items():
        water = sum_water(indexes)
        total_water += water

    return total_water


def sum_water(indexes: List[int]) -> int:
    prev_index = indexes[0] - 1
    total_water = 0
    for index in indexes:
        diff = index - prev_index
        water = diff - 1
        total_water += water
        prev_index = index

    return total_water
