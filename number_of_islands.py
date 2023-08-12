class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        num_islands = 0

        def explore(i, j):
            nonlocal visited
            nonlocal grid
            visited[i][j] = True
            if i-1 >= 0 and not visited[i-1][j] and grid[i-1][j] == '1':
                explore(i-1, j)
            if i+1 < m and not visited[i+1][j] and grid[i+1][j] == '1':
                explore(i+1, j)            
            if j-1 >= 0 and not visited[i][j-1] and grid[i][j-1] == '1':
                explore(i, j-1)
            if j+1 < n and not visited[i][j+1] and grid[i][j+1] == '1':
                explore(i, j+1)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    explore(i, j)
                    num_islands += 1
        
        return num_islands