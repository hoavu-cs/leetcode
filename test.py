    def same_char(self, s):
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                return False
        return True

    def isMatch(self, s: str, p: str) -> bool:
        """
        Recursive solution.
        Let M[i+1,j+1] = true if and only if s[0...i] matches with p[0...j]
        Consider these two substrings. Note that there are these cases:
        -- Case 1: s[i] != p[j] and neither are {*,-} then they cannot be matched 
        -- Case 2: s[i] = p[j] and neither are {*,-} then they can be matched iff M[i, j] is true
        -- Case 3: If s[i] = * then they can be matched iff any of M[i, k] is true for k <= j 
        as long as p[k+1...j] are the same character
        Similarly, if p[j] = * then they can be matched iff any of M[k, j] is true for k <= i
        as long as p[k+1...j] are the same character
        -- Case 4: If s[i] = -, then they can be matched iff M[i-1, j-1] is true
        Similarly, if s[j] = -, then they can be matched iff M[i-1, j-1] is true    
        """
        n = len(s)
        m = len(p)
        M = [[False for j in range(m+1)] for i in range(n+1)]
        
        # base cases
        M[0][0] = True
        for i in range(1, n+1):
            if s[i-1] != '*':
                M[i][0] = False
            else: 
                M[i][0] = M[i-1][0] 
        for j in range(1, m+1):
            if p[j-1] != '*':
                M[0][j] = M[0][j-1]
            else:
                M[0][j] = False
        # filling the dynamic programing table
        special = ['*', '.']
        for i in range(1, n):
            for j in range(1, m):
                if (s[i] not in special) and (p[j] not in special):
                    if s[i] != p[j]:
                        M[i][j] = False
                    else:
                        M[i][j] = M[i-1][j-1]
                elif s[i] == '*':
                    for k in range(j):
                        if (self.same_char(p[k:j]) == True) and (M[i-1][k] == True):
                            M[i][j] = True
                elif p[j] == '*':
                    for k in range(i):
                        if (self.same_char(s[k:i]) == True) and (M[k][j-1] == True):
                            M[i][j] = True
                elif s[i] == '.' or p[j] == '.':
                    M[i][j] = M[i-1][j-1]
        return M[n-1][m-1]


            

s = "mississippi"
p = "mis*is*p*."
     
solution = Solution()
print(solution.isMatch(s, p))