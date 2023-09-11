from math import inf

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [(-1, -inf)] 
        previous_less_than = [-1 for i in range(n)]
        for i in range(n):
            if heights[i] <= stack[-1][1]:
                while len(stack) > 0 and\
                        stack[-1][1] >= heights[i]:
                    stack.pop()
                previous_less_than[i] = stack[-1][0] 
            else:
                previous_less_than[i] = i-1
            stack.append((i, heights[i]))

        stack = [(n, -inf)] 
        next_greater_than = [n for i in range(n)]
        for i in range(n-1, -1, -1):
            if heights[i] <= stack[-1][1]:
                while len(stack) > 0 and\
                        stack[-1][1] >= heights[i]:
                    stack.pop()
                next_greater_than[i] = stack[-1][0]
            else:
                next_greater_than[i] = i+1
            stack.append((i, heights[i]))
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area,\
                heights[i]*(next_greater_than[i]\
                    -previous_less_than[i]-1))
        
        return max_area
