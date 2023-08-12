class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        linearized_nodes = [(matrix[i][j], (i, j)) for i in range(m) for j in range(n)]
        dp = [[1 for j in range(n)] for i in range(m)]
        res = 0
        
        # topological sort the graph 
        linearized_nodes = sorted(linearized_nodes, key=lambda x: x[0])

        for k in range(m*n-1, -1, -1):
            i, j = linearized_nodes[k][1][0],  linearized_nodes[k][1][1]
            if i-1 >=0 and matrix[i-1][j] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + 1)
            if i+1 < m and matrix[i+1][j] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dp[i+1][j] + 1)            
            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
            if j+1 < n and matrix[i][j+1] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dp[i][j+1] + 1)
            res = max(res, dp[i][j])
        
        return res

