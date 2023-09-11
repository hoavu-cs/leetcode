from math import inf

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Compute the largest rectangle given histogram bars
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

    def maximalRectangle(self, matrix: List[List[str]]):
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        max_area = 0
        
        # base cases
        current_run = 0
        for j in range(n):
            if matrix[0][j] == '1':
                current_run += 1
                dp[0][j] = int(matrix[0][j] == '1')
                max_area = max(current_run, max_area)
            else:
                current_run = 0
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i-1][j] + 1
                r = inf
                k = j
            histogram = [dp[i][j] for j in range(n)]
            max_area_of_row_i = self.largestRectangleArea(histogram)
            max_area = max(max_area, max_area_of_row_i) 
        
        return max_area
