import unittest
import add_numbers


class TestMakeLL(unittest.TestCase):
    def test_make_long_number(self):
        number = 12345
        list_creator = add_numbers.Solution().create_linked_list
        head_node = list_creator(number)
        self.assertEqual(head_node.val, 5)
        self.assertEqual(head_node.next.val, 4)
        self.assertEqual(head_node.next.next.val, 3)
        self.assertEqual(head_node.next.next.next.val, 2)
        self.assertEqual(head_node.next.next.next.next.val, 1)
        self.assertEqual(head_node.next.next.next.next.next, None)


class TestAddNumbers(unittest.TestCase):
    def setUp(self):
        solution = add_numbers.Solution()
        self.list_creator = solution.create_linked_list
        self.adder = solution.addTwoNumbers

    def test_two_zeros(self):
        int_1 = 0
        int_2 = 0
        l1_head = self.list_creator(int_1)
        l2_head = self.list_creator(int_2)
        sum_head = self.adder(l1_head, l2_head)
        self.assertEqual(0, sum_head.val)


if __name__ == '__main__':
    unittest.main()
