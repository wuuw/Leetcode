# Define binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def serialize(self, root: 'TreeNode'):
        return self.__serialize_helper(root, [])


    def deserialize(self, data):
        root, _ = self.__deserialize_helper(TreeNode(None), data)
        return  root


    def __serialize_helper(self, root: 'TreeNode', data):
        if not root:
            data.append('null')
        else:
            data.append(root.val)
            data = self.__serialize_helper(root.left, data)
            data = self.__serialize_helper(root.right, data)
        return data


    def __deserialize_helper(self, root: 'TreeNode', data):
        val = data.pop(0)
        if val == 'null':
            return None, data
        else:
            root.val = val
            root.left, data = self.__deserialize_helper(TreeNode(None), data)
            root.right, data = self.__deserialize_helper(TreeNode(None), data)
            return root, data