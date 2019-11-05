import unittest
import rainwater

class TestRainWater(unittest.TestCase):

    def test_bowl(self):
        heightmap = [0,1,0,1,0]
        total = 1
        self.assertEqual(total, rainwater.trap(heightmap))

    def test_hill(self):
        heightmap = [0,1,0]
        total = 0
        self.assertEqual(total, rainwater.trap(heightmap))

    def test_caldera(self):
        heightmap = [0,3,0,1,0,3]
        total = 8
        self.assertEqual(total, rainwater.trap(heightmap))

    def test_peak(self):
        heightmap = [0,1,2,3,2,1,0]
        total = 0
        self.assertEqual(total, rainwater.trap(heightmap))

    def test_foothils(self):
        heightmap = [0,1,2,1,2,3,2,1,2,1,0]
        total = 2
        self.assertEqual(total, rainwater.trap(heightmap))

    def test_cirque(self):
        heightmap = [0,3,1,0,5,0]
        total = 5
        self.assertEqual(total, rainwater.trap(heightmap))

    def test_valley(self):
        heightmap = [3,2,1,3]
        total = 3
        self.assertEqual(total, rainwater.trap(heightmap))

    def test_leetcode_example(self):
        heightmap = [0,1,0,2,1,0,1,3,2,1,2,1]
        total = 6
        self.assertEqual(total, rainwater.trap(heightmap))

if __name__ == '__main__':
    unittest.main()
