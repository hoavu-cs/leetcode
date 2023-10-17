from math import inf
from bisect import bisect_left, bisect_right
from collections import defaultdict

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # true if one can reach the end starting with an even jump
        even_reachable = [False for _ in range(n)]
        # true if one can reach the end starting with an odd jump
        odd_reachable = [False for _ in range(n)]
        res = 1
                
        # precompute odd/even jumps
        odd_jump = [-1 for i in range(n)]
        even_jump = [-1 for i in range(n)]
        even_reachable[n - 1] = odd_reachable[n - 1] = True
        q = [arr[n-1]]
        first_occurence = defaultdict(int)
        first_occurence[arr[n-1]] = n-1

        for i in range(n - 2, -1 , -1):
            idx = bisect_left(q, arr[i])
            if idx < len(q):
                odd_reachable[i] = even_reachable[first_occurence[q[idx]]]

            idx = bisect_right(q, arr[i])
            if idx > 0:
                even_reachable[i] = odd_reachable[first_occurence[q[idx - 1]]]

            q.insert(idx, arr[i])
            first_occurence[arr[i]] = i

            if odd_reachable[i]:
                res += 1

        return res

