class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

########################
###     快慢指针     ###
########################

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
            if slow == fast:
                return slow
            if not fast.next:
                return False
            else:
                slow, fast = slow.next, fast.next.next
        return False


"""
if __name__ == "__main__":
    s = Solution()
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = head.next.next

    print(s.detectCycle(head))
"""