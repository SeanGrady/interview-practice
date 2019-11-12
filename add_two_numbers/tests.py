import unittest
import add_numbers


class TestMakeLL(unittest.TestCase):
    def setUp(self):
        self.solution = add_numbers.Solution()
        self.list_creator = self.solution.create_linked_list
        self.number_creator = self.solution.linked_list_to_int


    def test_make_long_number(self):
        number = 12345
        head_node = self.list_creator(number)
        self.assertEqual(head_node.val, 5)
        self.assertEqual(head_node.next.val, 4)
        self.assertEqual(head_node.next.next.val, 3)
        self.assertEqual(head_node.next.next.next.val, 2)
        self.assertEqual(head_node.next.next.next.next.val, 1)
        self.assertEqual(head_node.next.next.next.next.next, None)

    def test_list_to_int(self):
        number = 2318473
        number_list = self.list_creator(number)
        recovered_number = self.number_creator(number_list)
        self.assertEqual(number, recovered_number)

    def test_zero_both_directions(self):
        number = 0
        number_list = self.list_creator(number)
        recovered_number = self.number_creator(number_list)
        self.assertEqual(number, recovered_number)

class TestAddNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = add_numbers.Solution()
        self.list_creator = self.solution.create_linked_list
        self.adder = self.solution.addTwoNumbers
        self.number_creator = self.solution.linked_list_to_int

    def test_two_zeros(self):
        int_1 = 0
        int_2 = 0
        answer = 0
        l1_head = self.list_creator(int_1)
        l2_head = self.list_creator(int_2)
        sum_head = self.adder(l1_head, l2_head)
        sum_int = self.number_creator(sum_head)
        self.assertEqual(answer, sum_int)

    def test_single_digits(self):
        int_1 = 5
        int_2 = 3
        answer = 8
        head_1 = self.list_creator(int_1)
        head_2 = self.list_creator(int_2)
        sum_head = self.adder(head_1, head_2)
        sum_int = self.number_creator(sum_head)
        self.assertEqual(answer, sum_int)


if __name__ == '__main__':
    unittest.main()
