class Solution:
    def romanToInt(self, s: str) -> int:
        
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        n = len(s)
        t = 0
        sum = 0

        while t<n:
            l = list()
            if t == n-1:
                sum += d[s[t]]
                t +=1
            elif d[s[t]] < d[s[t+1]]:
                sum += d[s[t+1]] - d[s[t]]
                t += 2
            else:
                sum += d[s[t]]
                t += 1

        return sum

#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s = input()
    ans = sol.romanToInt(s)
    print(ans)