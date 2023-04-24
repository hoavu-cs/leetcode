class Solution:

    def diff(self, x: str, y: str) -> int:  
        if x == y:
            return 0
        else:
            return 1

    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        word1 = " " + word1 
        word2 = " " + word2
        # initialize the dynamic programming table n by m
        ED = [[0 for x in range(m+2)] for y in range(n+2)]
        
        # fill the DP table as described
        for i in range(n+1):
            for j in range(m+1):
                if i == 0: # first base case
                    ED[i][j] = j
                elif j == 0: # second base case
                    ED[i][j] = i
                else: # computing ED[i,j] recursively
                    ED[i][j] = min(ED[i-1][j]+1, ED[i][j-1]+1, self.diff(word1[i],word2[j]) + ED[i-1][j-1])
        return ED[n][m]