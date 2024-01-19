from collections import defaultdict
from math import inf

class Solution:
    dp = {}
    palindromes = set()

    def precomputePalindromes(self, s):
        for k in range(len(s)):
            for i in range(len(s) - k):
                if k == 0:
                    self.palindromes.add(s[i])
                elif k == 1 and s[i] == s[i + 1]:
                    self.palindromes.add(s[i:i + k + 1])
                elif s[i] == s[i + k] and s[i + 1:i + k] in self.palindromes:
                    self.palindromes.add(s[i:i + k + 1])
    
    def minCutSolver(self, s):
        if s in self.palindromes:
            self.dp[s] = 0
        else:
            n = len(s)
            self.dp[s] = inf

            for i in range(n):
                prefix, suffix = s[:i], s[i:]
                if prefix in self.palindromes:
                    if prefix not in self.dp:
                        self.minCutSolver(prefix)
                    if suffix not in self.dp:
                        self.minCutSolver(suffix)
                    self.dp[s] = min(self.dp[prefix] + self.dp[suffix] + 1, self.dp[s])

    def minCut(self, s: str) -> int:
        self.precomputePalindromes(s)
        self.minCutSolver(s)
        return self.dp[s]


                





        
