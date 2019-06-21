class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
解题思路：
（1）首先通过快慢指针的方法判断链表是否有环；
（2）接下来如果有环，则寻找入环的第一个节点。
具体的方法为，首先假定链表起点到入环的第一个节点A的长度为a【未知】，
到快慢指针相遇的节点B的长度为（a + b）【这个长度是已知的】。
现在我们想知道a的值，注意到快指针p2始终是慢指针p走过长度的2倍，
所以慢指针p从B继续走（a + b）又能回到B点，如果只走a个长度就能回到节点A。
但是a的值是不知道的，解决思路是曲线救国，注意到起点到A的长度是a，
那么可以用一个从起点开始的新指针q和从节点B开始的慢指针p同步走，
相遇的地方必然是入环的第一个节点A。

a + b = a1 + a2 + a3 + a4 + b
a = a1 + a2 + a3 + a4

|   a   |  b  | a1
------------------
    a4  |        | a2
        |        |
        ----------
            a3
"""
class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return False
        slow, fast = head, head
        '''寻找环'''
        while slow and fast:
            '''无环'''
            if not fast.next:
                return False
            else:
                slow = slow.next
                fast = fast.next.next

            '''有环'''
            if slow == fast:
                '''开始寻找入口节点'''
                slow, index = head, 0
                while True:
                    slow = slow.next
                    fast = fast.next
                    index += 1
                    if slow == fast:
                        return index
        return False


'''
if __name__ == "__main__":
    s = Solution()
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = head.next.next

    print(s.detectCycle(head))
'''
