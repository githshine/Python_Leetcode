# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
#     Merge the two lists into one sorted list. 

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = current = ListNode(0, None)
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # attach the remaining part
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return head.next


def build_list(vals):
    """Build a linked list from a Python list of values and return head."""
    head = cur = None
    for v in vals:
        node = ListNode(v)
        if cur:
            cur.next = node
            cur = cur.next
        else:
            head = cur = node
    return head


def to_list(head: Optional[ListNode]):
    """Convert linked list to Python list of values."""
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


if __name__ == '__main__':
    obj = Solution()
    l1 = build_list([])
    l2 = build_list([0])
    merged = obj.mergeTwoLists(l1, l2)
    print(to_list(merged))