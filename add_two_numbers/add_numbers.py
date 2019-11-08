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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        
