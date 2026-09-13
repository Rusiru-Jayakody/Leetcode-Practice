class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for i in asteroids:
            while stk and stk[-1] > 0 and i < 0:
                x = stk.pop()
                diff = x + i
                if diff > 0:
                    i = x
                elif diff < 0:
                    i = i
                else:
                    i = 0
            if i:
                stk.append(i)
        return stk


