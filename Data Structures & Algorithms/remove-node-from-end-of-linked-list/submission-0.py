# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        if not cur:
            return None
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        removeidx = len(nodes)-n
        if removeidx == 0:
            return head.next
        nodes[removeidx-1].next = nodes[removeidx].next
        return head