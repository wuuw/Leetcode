# Define binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def serialize(self, root: 'TreeNode'):
        if not root:
            return '$,'
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)


    def deserialize(self, data):
        data = data.split(',')[0:-1]
        root, _ = self.__deserialize_helper(TreeNode(None), data)
        return  root


    def __deserialize_helper(self, root: 'TreeNode', data):
        val = data.pop(0)
        if val == '$':
            return None, data
        else:
            root.val = int(val)
            root.left, data = self.__deserialize_helper(TreeNode(None), data)
            root.right, data = self.__deserialize_helper(TreeNode(None), data)
            return root, data