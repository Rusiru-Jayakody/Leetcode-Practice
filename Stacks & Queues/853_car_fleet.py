class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        temp = []
        for i in range(len(position)):
            temp.append([position[i],speed[i]])
        temp.sort(key = lambda x: x[0])
        for i in range(len(temp)):
            temp[i] = (target - temp[i][0]) / temp[i][1]
        count = 0
        stk = []

        for i in range(len(temp)-1,-1,-1):
            if not stk:
                stk.append(temp[i])
                count += 1
            else:
                if stk[-1] >= temp[i]:
                    pass
                else:
                    stk.pop()
                    stk.append(temp[i])
                    count += 1
        return count
            
        