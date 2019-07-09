# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.cloneNodes(head)
        self.linkRandomNodes(head)
        return self.unpackLink(head)

    # 构建 A -> A' -> B -> B' ... 链表
    def cloneNodes(self, head: 'Node'):
        pNode = head
        while pNode:
            pClone = Node(pNode.val, None, None)
            pClone.next = pNode.next
            pNode.next = pClone
            pNode = pClone.next

    # 补充上一步链表中克隆节点的 random 指针
    def linkRandomNodes(self, head: 'Node'):
        pNode = head
        while pNode:
            pClone = pNode.next
            if pNode.random:
                pClone.random = pNode.random.next
            pNode = pClone.next

    def unpackLink(self, head: 'Node'):
        pNode, new, pNew = head, None, None
        if pNode:
            new = pNew = pNode.next
            pNode.next = pNew.next
            pNode = pNode.next

        while pNode:
            pNew.next = pNode.next
            pNew = pNew.next
            pNode.next = pNew.next
            pNode = pNode.next
        return new