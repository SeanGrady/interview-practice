from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        side_counts = {
            'A': {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
            },
            'B': {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
            },
        }
        num_dominos = len(A)
        value_counts = {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
            }

        for i in range(num_dominos):
            top = A[i]
            bot = B[i]
            if top == bot:
                value_counts[top] += 1
            else:
                value_counts[top] += 1
                value_counts[bot] += 1
                side_counts['A'][top] += 1
                side_counts['B'][bot] += 1

        max_value = max(value_counts, key=lambda x: value_counts[x])
        max_value_total = value_counts[max_value]
        if max_value_total < num_dominos:
            return -1
        A_count = side_counts['A'][max_value]
        B_count = side_counts['B'][max_value]

        if A_count == num_dominos:
            return 0
        if B_count == num_dominos:
            return 0

        return min(A_count, B_count)
