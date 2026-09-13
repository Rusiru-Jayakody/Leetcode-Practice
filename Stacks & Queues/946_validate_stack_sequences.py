class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = set()
        stk = []
        x,y = 0, 0

        while x < len(pushed) or y < len(popped):
            while x < len(pushed) and popped[y] not in s:
                stk.append(pushed[x])
                s.add(pushed[x])
                x += 1
            
            while y < len(popped) and popped[y] in s:
                if stk and stk[-1] == popped[y]:
                    stk.pop()
                    y += 1
                else:
                    return False
        return True


        