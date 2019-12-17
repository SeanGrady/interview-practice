from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        for index, value in enumerate(nums):
            complement = target - value
            if value in complement_map:
                first_index = complement_map[value]
                second_index = index
                return [first_index, second_index]

            complement_map[complement] = index

