class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for c in s:
            if c != '*':
                stk.append(c)
            elif stk and c == '*':
                stk.pop()
        
        return "".join(stk)
        