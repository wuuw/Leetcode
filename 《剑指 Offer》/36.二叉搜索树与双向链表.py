# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 递归地树链表化
        lastNodeInList = self.helper(root, None)
        # 此时 lastNodeInList 指向双向链表尾节点，需要返回头节点
        head = lastNodeInList
        while head and head.left:
            head = head.left
        if head:
            head.left = lastNodeInList
            lastNodeInList.right = head
        return head

    # 递归函数
    def helper(self, root: 'Node', lastNodeInList):
        if not root:
            return

        # 首先递归来到树的先序遍历第一个节点
        cur = root
        if cur.left:
            lastNodeInList = self.helper(cur.left, lastNodeInList)

        # 递归的最内层来到先序遍历第一个节点，left 指向此时的 lastNodeInList(空)
        # 如果返回递归的外层，来到上一个根节点, left 指向内层已经链表化的最后一个节点
        cur.left = lastNodeInList

        # 如果不是递归最内层，已经链表化的最后一个节点也要 right 向下一个节点
        if lastNodeInList:
            lastNodeInList.right = cur

        # 更新 lastNodeInList 节点
        lastNodeInList = cur

        if cur.right:
            lastNodeInList = self.helper(cur.right, lastNodeInList)

        return lastNodeInList