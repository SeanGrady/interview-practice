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

    def test_two_zeros(self):
        pass


if __name__ == '__main__':
    unittest.main()
