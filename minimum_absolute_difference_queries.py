from math import inf
import copy 
from bisect import bisect_left

class Solution:
    def binary_search(self, L, x):
        i = bisect_left(L, x)
        if i < len(L):
            if L[i] == x:
                return i
            else:
                return None
        else:
            return None

    def minDifference(self, nums, queries):
        n = len(nums)
        ans = [inf for i in range(len(queries))]
        distinct_sets = {}
        S = {}

        query_points = set([q[0] for q in queries] + [q[1] for q in queries])
        query_points = sorted(list(query_points))

        for i  in range(n):
            if nums[i] in S:
                S[nums[i]] += 1
            else:
                S[nums[i]] = 1
            if self.binary_search(query_points, i) or self.binary_search(query_points, i+1) != None: 
                distinct_sets[i] = copy.copy(S)
        
        for i, q in enumerate(queries):
            elms = []
            if q[0] == 0:
                elms = [e for e in distinct_sets[q[1]].keys()]
            else:
                for e in distinct_sets[q[1]].keys():
                    elms.append(e)
                    if e in distinct_sets[q[0]-1] and \
                    distinct_sets[q[1]][e] - distinct_sets[q[0]-1][e] == 0:
                        elms.pop()
            elms = sorted(elms)
            for j in range(len(elms)-1):
                if ans[i] > abs(elms[j]-elms[j+1]) and abs(elms[j]-elms[j+1]) > 0: 
                    ans[i] =  abs(elms[j]-elms[j+1])
            if ans[i] == inf: ans[i] = -1
        return ans