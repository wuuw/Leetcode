# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        p1, p2 = headA, headB
        # 当两个链表长度相等，若没有交点，第一轮同时走到链表末尾就会 None == None，最终返回 None
        # 当两个链表长度不等，会在来到对方链表末尾是 None == None，最终返回 None
        # 如果有交点，要么在各自链上时相遇（长度相等），要么在对方链上时相遇相遇（长度不等）
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
