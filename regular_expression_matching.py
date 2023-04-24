class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        # change indexing from 1 to make life simpler
        s = "$" + s 
        p = "$" + p

        # M[i,j] = true iff s[0...i] can be matched with p[0...j]        
        M = [[False for j in range(m+1)] for i in range(n+1)]

        M[0][0] = True # true since two empty strings can be matched
        for j in range(1, m+1):
            if p[j] == '*' and j >= 2:
                M[0][j] = M[0][j-2]
        
        specials =  ['*', '.']
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j] not in specials:
                    M[i][j] = (s[i] == p[j]) and (M[i-1][j-1])
                else:
                    if p[j] == '.':
                        M[i][j] = M[i-1][j-1]
                    else:
                        if M[i][j-2] == True:
                            M[i][j] = True
                        else:
                            if p[j-1] != '.':
                                for k in range(i+1):
                                    if s[k:i+1] == p[j-1]*(i-k+1) and M[k-1][j-2]:
                                        M[i][j] = True
                            else:
                                for k in range(i+1):
                                    if M[k-1][j-2]:
                                        M[i][j] = True
        return M[n][m]
