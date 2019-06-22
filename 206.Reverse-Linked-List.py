# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

''' 1. 递归方法实现 '''

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        """
            将问题转化为 head 节点与 head.next 链的反转链表连接问题
        """
        # 没有到达末尾
        if head:
            sub = self.reverseList(head.next)
            # 返回到达末尾的结果
            if not sub:
                return head
            # 返回非末尾的结果
            else:
                p = sub
                while p.next:
                    p = p.next
                p.next = head
                head.next = None
                return sub
        # 到达末尾
        else:
            return None


''' 2. 栈方法实现'''

class Solution2(object):
    def reverseList(self, head: ListNode) -> ListNode:
        """
            顺序入栈，出栈重构链表
        """
        # 进栈
        if not head: return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        # 出栈
        head, p = None, None
        while stack:
            p = stack.pop(0)
            p.next = head
            head = p
        return p


''' 3. 迭代方法实现 '''

class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        """
            依次将节点指向上一个节点
            防止链断裂，需要保存当前节点的 next 节点
        """
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
            """
            next = p.next
            p.next = rev
            rev = p
            p = next
            """
        return rev