# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        """
            before: 如题中的 1
            entry: 如题中的 2
            rev: 区间的反转链表
            next: 指示下一个节点
        """
        p, before, entry, rev = head, None, None, None
        i = 1

        while p:
            if i < m:  # 寻找入口
                before = p
                p = p.next
            elif (i >= m) and (i <= n):  # 反转区间链表
                if i == m: entry = p  # 保存 entry

                next = p.next
                p.next = rev
                rev = p
                p = next
            else:
                break
            i += 1

        entry.next = p # 连接 n 后的节点
        if m != 1:     # 连接 m 前的节点
            before.next = rev
            rev = head
        return rev