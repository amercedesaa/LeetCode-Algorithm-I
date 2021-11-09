# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = head2 = head
        while head2 and head2.next:
            head1 = head1.next
            head2 = head2.next.next
        return head1
