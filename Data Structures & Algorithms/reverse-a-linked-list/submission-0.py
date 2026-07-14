# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        tail = None
        cur = head
        previous = []
        while cur.next != None:
            previous.append(cur)
            cur = cur.next
        tail = cur
        while cur != head:
            prev_node = previous.pop()
            cur.next = prev_node
            cur = prev_node
        head.next = None
        return tail



        