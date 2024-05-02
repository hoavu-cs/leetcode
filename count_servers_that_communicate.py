class Node:
    def __init__(self, x, y):
        self.coordinates = (x, y)
        self.parent = self
        self.rank = 0
        self.size = 1

def makeSet(i, j):
    return Node(i, j)

def find(x):
    while x.parent != x:
        x = x.parent
    return x

def union(x, y):
    rx = find(x)
    ry = find(y)

    if rx == ry:
        return

    if rx.rank > ry.rank:
        ry.parent = rx
        rx.size += ry.size
    else:
        rx.parent = ry
        ry.size += rx.size
        if rx.rank == ry.rank:
            ry.rank += 1

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        nodes = {} 

        for i in range(m):
            previous = None
            for j in range(n):
                if grid[i][j] == 1:
                    server = makeSet(i, j)
                    nodes[(i, j)] = server
                    if previous != None:
                        union(server, previous)
                    else:
                        previous = server
        
        for j in range(n):
            previous = None
            for i in range(m):
                if grid[i][j] == 1:
                    server = nodes[(i, j)]
                    if previous != None:
                        union(server, previous)
                    else:
                        previous = server
        ans = 0
        for x in nodes:
            server = nodes[x]
            if find(server).size > 1:
                ans += 1
                
        return int(ans)
