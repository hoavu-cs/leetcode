class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                if (stack[-1] == '(' and s[i] == ')') or (stack[-1] == '[' and s[i] == ']') or \
                (stack[-1] == '{' and s[i] == '}'):
                    stack.pop(-1)
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True 
