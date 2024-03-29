class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

########################
###     快慢指针     ###
########################

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        '''initialize fast / slow'''
        slow, fast = head, head.next
        '''run them'''
        while fast and slow:
            '''fast and slow meet'''
            if fast == slow:
                return True
            ''''''
            if not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return False