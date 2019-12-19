import unittest
import sortchecker

class TestSortChecker(unittest.TestCase):
    def setUp(self):
        self.checker = sortchecker.Solution().isAlienSorted

    def test_leetcode_testcase(self):
        words = ["hello","leetcode"]
        alphabet = "hlabcdefgijkmnopqrstuvwxyz"
        answer = True
        result = self.checker(words, alphabet)
        self.assertEqual(answer, result)

    def test_leetcode_testcase2(self):
        words = ["word","world","row"]
        alphabet = "worldabcefghijkmnpqstuvxyz"
        answer = False
        result = self.checker(words, alphabet)
        self.assertEqual(answer, result)

    def test_leetcode_testcase3(self):
        words = ["apple","app"]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        answer = False
        result = self.checker(words, alphabet)
        self.assertEqual(answer, result)

if __name__ == '__main__':
    unittest.main()
