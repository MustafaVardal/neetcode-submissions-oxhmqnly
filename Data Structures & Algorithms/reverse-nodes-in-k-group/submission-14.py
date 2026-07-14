# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        curr = dummy
     

        while True:
            kth = self.getKth(curr, k)
            if not kth:
                break
            nxt = kth.next

            prev, now = kth.next, curr.next

            while now != nxt:
                tmp = now.next
                now.next = prev
                prev = now
                now = tmp
            
            temp = curr.next
            curr.next = kth
            curr = temp
        return dummy.next

            
    def getKth(self, curr, k):

        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
