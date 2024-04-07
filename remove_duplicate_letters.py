from collections import Counter 

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        suffix_set = Counter(s)
        stack_set = set()
        ans_set = set()
        stack = []
        ans = ""
        
        for c in s:
            suffix_set[c] -= 1
            if c in stack_set or c in ans_set:
                continue
            
            while len(stack) > 0 and stack[-1] > c and suffix_set[stack[-1]] > 0:
                print("pop ", stack[-1])
                stack_set.remove(stack[-1])
                stack.pop()
            
            if len(stack) > 0 and stack[-1] > c:
                for i in range(len(stack)):
                    ans += stack[i]
                    ans_set.add(stack[i])
                stack = []

            stack.append(c)
            stack_set.add(c)

        for i in range(len(stack)):
            ans += stack[i]
        
        return ans

            

            





        
                


