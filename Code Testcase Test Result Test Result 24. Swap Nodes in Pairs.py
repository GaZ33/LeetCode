# I beats 100% runtime and 82.29% memory


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head

        anterior = head
        head = head.next

        anterior.next = head.next
        head.next = anterior

        posterior = anterior.next

        while anterior.next != None and posterior.next != None :
            posterior2 = posterior.next
            anterior.next = posterior2
            posterior.next = posterior2.next
            posterior2.next = posterior
            anterior = posterior
            posterior = anterior.next
        
        return head
