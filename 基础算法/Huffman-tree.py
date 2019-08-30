# 创建节点类
class Node:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Huffman:

    def build(self, nums):
        # 构建森林
        forest = [Node(i) for i in nums]

        if not forest: return None
        if len(forest) == 1:
            merged = Node(forest[0].val)
            merged.left = forest[0]
            return merged

        while len(forest) > 1:
            # 对森林进行排序
            forest = self.sort_forest(forest)
            # 获取森林中两个最小树
            a, b = forest.pop(), forest.pop()
            # 合并节点，并加入到森林中
            merged = Node(a.val + b.val)
            merged.left = b
            merged.right = a
            forest.append(merged)

        return forest[0]


    def sort_forest(self, forest):
        """
        基于森林中每棵树根节点的值排序
        :param forest: 森林-树的列表
        :return: 增序列表
        """
        return sorted(forest, key=lambda k: k.val, reverse=True)


if __name__ == "__main__":
    huffman = Huffman()
    tree = huffman.build([15, 8, 6, 5, 3, 1])
    pass