import unittest
import twosum

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.two_sum = twosum.Solution().twoSum

    def test_leetcode_testcase(self):
        integers = [2, 7, 11, 15]
        target = 9
        answer = [0, 1]
        indices = self.two_sum(integers, target)
        self.assertEqual(answer, indices)

if __name__ == '__main__':
    unittest.main()
