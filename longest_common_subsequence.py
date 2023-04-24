class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        n = len(text1)
        m = len(text2)     
        text1 = " " + text1
        text2 = " " + text2        
        LCS = [[0 for x in range(m+1)] for y in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    LCS[i][j] = 0
                else:
                    if text1[i] == text2[j]:
                        LCS[i][j] = LCS[i-1][j-1]+1
                    else:
                        LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
                    
        return LCS[n][m]