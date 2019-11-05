from typing import List
from collections import defaultdict


def trap(heightmap: List[int]) -> int:
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
