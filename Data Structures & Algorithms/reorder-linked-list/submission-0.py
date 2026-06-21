# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 3 steps:
        # slow and fast to find middle. when fast reaches end, slow will be at middle
        # take second half and reverse it
        # join the two in the zipper strategy

        # Handle empty list or list of 1 or 2 elements
        if not head or not head.next or not head.next.next:
            return

        # 1. Find middle
        slow = head
        fast = head
        while fast and fast.next:
            prev_mid = slow
            slow = slow.next
            fast = fast.next.next

            if fast == None:
                break

        if prev_mid:
            prev_mid.next = None
        
        # now, slow contains second half

        # 2. Reverse second half
        prev = None
        current = slow
        next_node = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # now, prev contains second half reversed

        # 3. Zipper
        first = head
        second = prev
        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second

            if temp1 is None:
                break

            second.next = temp1

            first = temp1
            second = temp2