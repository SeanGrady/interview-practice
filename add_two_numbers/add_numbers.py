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
        current_node = head
        while current_node.next:
            current_node = current_node.next
            digit_list.append(current_node.val)

        digit_list.reverse()
        added = int("".join(map(str, digit_list)))
        return added

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_node_1 = l1
        current_node_2 = l2
        carry = 0
        next_digit, carry = self.add_digits(current_node_1.val, current_node_2.val, carry)
        sum_head = ListNode(next_digit)
        current_sum_node = sum_head

        if current_node_1.next:
            current_node_1 = current_node_1.next
        else:
            current_node_1 = None
            
        if current_node_2.next:
            current_node_2 = current_node_2.next
        else:
            current_node_2 = None

        while current_node_1 or current_node_2 or carry:
            if not current_node_1:
                current_digit_1 = 0
            else:
                current_digit_1 = current_node_1.val
            if not current_node_2:
                current_digit_2 = 0
            else:
                current_digit_2 = current_node_2.val

            next_digit, carry = self.add_digits(current_digit_1, current_digit_2, carry)
            next_node = ListNode(next_digit)

            current_sum_node.next = next_node
            current_sum_node = next_node

            if current_node_1 and current_node_1.next:
                current_node_1 = current_node_1.next
            else:
                current_node_1 = None
                
            if current_node_2 and current_node_2.next:
                current_node_2 = current_node_2.next
            else:
                current_node_2 = None

        return sum_head


    def add_digits(self, int1: int, int2: int, carry: int):
        if not carry:
            carry = 0

        total = int1 + int2 + carry
        if total < 10:
            new_carry = 0
        else:
            total = total % 10
            new_carry = 1

        return total, new_carry
