# Define ListNode class
class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

"""
递归法
1. 首先判断 l1/l2 中是否含有空链表，如果有则返回另一个链表
2. 首先判断两个链表的头节点值，将较小者保存作为新链表的值
3. 该新链表的 next 指向两个链表剩余节点的排序链表
4. 上述过程采用递归实现
"""
class Solution(object):

    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        list = ListNode(0)

        if l1.val > l2.val:
            list.val = l2.val
            list.next = self.mergeTwoLists(l1, l2.next)
        else:
            list.val = l1.val
            list.next = self.mergeTwoLists(l1.next, l2)

        return list
                