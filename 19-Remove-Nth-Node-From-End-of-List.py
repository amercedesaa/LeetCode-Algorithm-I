# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head1 = head1p1 = head
        for i in range(n):
            head1p1 = head1p1.next
        if head1p1 is None:
            head = head.next
            return head
        while head1p1.next is not None:
            head1p1 = head1p1.next
            head1 = head1.next
        head11= head1.next
        head1.next = head11.next
        return head
