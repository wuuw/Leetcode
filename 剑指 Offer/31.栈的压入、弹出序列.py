"""
借助辅助栈
1. 如果下一个弹出的数字恰好在辅助栈顶，则直接弹出
2. 如果不在，就在压栈序列中还没入栈的数字中查找
3. 如果找到了，依次入栈直到该数字
4. 如果没找到，False
5. 最后 while 循环结束，说明验证完了
"""
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        # 都空 True
        if not pushed and not popped:
            return True
        # 长度不一致 False
        if len(pushed) != len(popped):
            return False

        aux = []
        pPush, pPop = 0, 0
        while pPop < len(popped):
            p = popped[pPop]
            # 在辅助栈顶找到
            if aux and aux[-1] == p:
                aux.pop()
                pPop += 1
                continue
            # 不在辅助栈顶，但在剩余 push 序列
            if p in pushed[pPush:]:
                while pushed[pPush] != p:
                    aux.append(pushed[pPush])
                    pPush += 1
                pPush += 1
                pPop += 1
            else:
                return False
        # 输出序列验证完了
        return True