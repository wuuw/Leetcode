class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = self.hasCycle(head)
        '''no cycle'''
        if not node: return False
        '''with cycle, to calculate num of nodes in loop'''
        num, p = 1, node
        while p.next != node:
            num += 1
            p = p.next
        '''find the entry'''
        slow, fast = head, head
        index = 0
        for i in range(num):
            fast = fast.next
        while fast.val != slow.val:
            fast = fast.next
            slow = slow.next
            index += 1
        return index

    def hasCycle(self, head):
        if not head: return False
        slow, fast = head, head.next
        while slow and fast:
            if slow.val == fast.val:
                return slow
            if not fast.next:
                return False
            else:
                slow, fast = slow.next, fast.next.next
        return False