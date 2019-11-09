# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def create_linked_list(self, number: int) -> ListNode:
        number_list = [int(char) for char in str(number)]
        number_list.reverse()
        head = ListNode(number_list[0])
        prev_node = head
        for value in number_list[1:]:
            node = ListNode(value)
            prev_node.next = node
            prev_node = node
        return head

    def linked_list_to_int(self, head: ListNode) -> int:
        digit_list = []
        digit_list.append(head.val)
        current_digit = head
        while current_digit.next:
            current_digit = current_digit.next
            digit_list.append(current_digit.val)

        digit_list.reverse()
        added = int("".join(map(str, digit_list)))
        return added

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1
