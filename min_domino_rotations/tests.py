import unittest
import solution


class TestDominoRotations(unittest.TestCase):
    def setUp(self):
        self.checker = solution.Solution()

    def test1(self):
        A = [2, 4, 5]
        B = [3, 1, 3]
        answer = -1
        result = self.checker.minDominoRotations(A, B)
        self.assertEqual(answer, result)

    def test2(self):
        A = [1,2,1]
        B = [3,1,4]
        answer = 1
        result = self.checker.minDominoRotations(A, B)
        self.assertEqual(answer, result)

    def test3(self):
        A = [1,1,1]
        B = [3,2,1]
        answer = 0
        result = self.checker.minDominoRotations(A, B)
        self.assertEqual(answer, result)

    def test4(self):
        A = [1,4]
        B = [3,1]
        answer = 1
        result = self.checker.minDominoRotations(A, B)
        self.assertEqual(answer, result)

    def test4(self):
        A = [1,3,5,1,2]
        B = [2,1,1,6,1]
        answer = 2
        result = self.checker.minDominoRotations(A, B)
        self.assertEqual(answer, result)

    def test5(self):
        A = [1,1,2]
        B = [1,2,3]
        answer = -1
        result = self.checker.minDominoRotations(A, B)
        self.assertEqual(answer, result)

    def test6(self):
        A = [2,1,2,4,2,2]
        B = [5,2,6,2,3,2]
        answer = 2
        result = self.checker.minDominoRotations(A, B)
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
