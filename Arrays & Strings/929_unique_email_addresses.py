class Solution:
    def numUniqueEmails(self, emails) -> int:
        s = set()
        for i in range(len(emails)):
            words = list(emails[i].split('@'))
            temp = []
            for j in range(len(words[0])):
                if words[0][j] == '.':
                    continue
                elif words[0][j] == '+':
                    break
                else:
                    temp.append(words[0][j])
            words[0] = ''.join(temp)
            x = '@'.join(words)
            if x not in s:
                s.add(x)
        return len(s)
        