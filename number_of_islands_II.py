
class Node:
    def __init__(self, x):
        self.val = x
        self.parent = self
        self.rank = 0

def find_set(x):
    while x.parent != x:
        x = x.parent
    return x

def union_set(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return False
    elif rx.rank > ry.rank:
        ry.parent = rx
        return True
    elif ry.rank > rx.rank:
        rx.parent = ry
        return True
    else:
        ry.parent = rx
        rx.rank += 1
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        land = {}
        counter = 0

        for i in range(len(positions)):
            r, c = positions[i]
            if (r, c) in land:
                ans.append(ans[-1])
                continue
            else:
                x = Node((r, c))
                land[(r, c)] = x
                counter += 1

            if r - 1 >= 0 and (r - 1, c) in land:
                y = land[(r - 1, c)]
                connect = union_set(x, y)
                if connect:
                    counter -= 1
            if c - 1 >= 0 and (r, c - 1) in land:
                y = land[(r, c - 1)]
                connect = union_set(x, y)
                if connect:
                    counter -= 1
            if r + 1 < m and (r + 1, c) in land:
                y = land[(r + 1, c)]
                connect = union_set(x, y)
                if connect:
                    counter -= 1
            if c + 1 < n and (r, c + 1) in land:
                y = land[(r, c + 1)]
                connect = union_set(x, y)
                if connect:
                    counter -= 1

            ans.append(counter)

        return ans           
        
