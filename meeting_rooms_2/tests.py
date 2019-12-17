import unittest
import meetingrooms

class TestMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.scheduler = meetingrooms.Solution().minMeetingRooms

    def test_leetcode_testcase(self):
        meetings = [[0, 30],[5, 10],[15, 20]]
        answer = 2
        result = self.scheduler(meetings)
        self.assertEqual(answer, result)

    def test_unsorted(self):
        meetings = [[7, 10], [2, 4]]
        answer = 1
        result = self.scheduler(meetings)
        self.assertEqual(answer, result)

if __name__ == '__main__':
    unittest.main()
