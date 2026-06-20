# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        head = None
        tail = None

        # Edge case handling
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        # Get first one
        if current1.val <= current2.val:
            head = current1
            current1 = current1.next
        else:
            head = current2
            current2 = current2.next
        tail = head

        # Choose lesser of two to be the next
        while current1 is not None and current2 is not None:
            if current1.val < current2.val:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        # Attach the remaining if one ends early
        if current1 is None and current2 is not None:
            tail.next = current2
        elif current2 is None and current1 is not None:
            tail.next = current1
            
        return head