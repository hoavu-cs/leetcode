from math import inf
class Solution:
    
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(s):
            count = 0
            for idx in range(len(s)):
                if s[idx] == '(':
                    count += 1
                elif s[idx] == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        added_strings = set()
        queue = [s]
        res = []
        maximal_valid = 0

        while len(queue) > 0:
            x = queue.pop(0)
            if x not in added_strings:
                added_strings.add(x)
                if is_valid(x):
                    maximal_valid = len(x)
                    res.append(x) 
                else:
                    if maximal_valid == 0:
                        for i in range(len(x)):
                            if x[i] in ['(', ')']:
                                y = x[:i] + x[i+1:]
                                queue.append(y)
            
        return res




