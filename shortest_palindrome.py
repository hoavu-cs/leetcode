class Solution:

    def longest_prefix_palindrome(self, s):
        # Return the longest palindrome that is a prefix of s
        # Modification of Manacher's algorithm
        s_padded = '#'


        for c in s:
            s_padded += c
            s_padded += '#'

        lelft, right = 1, -1
        s_padded = '$' + s_padded + '^'
        n = len(s_padded)
        p = [1 for i in range(0, n)]
        ans = 0

        for i in range(1, n - 1):
            if i > right:
                while s_padded[i - p[i]] == s_padded[i + p[i]]:
                    p[i] += 1
            else:
                p[i] = min(right - i, p[left + right - i])
                while s_padded[i - p[i]] == s_padded[i + p[i]]:
                    p[i] += 1

            p[i] -= 1

            if i + p[i] > right:
                left = i - p[i] 
                right = i + p[i]  

        for i in range(1, n - 1):
            if i - p[i] == 1:
                ans = max(ans, p[i])

        return ans

    def shortestPalindrome(self, s: str) -> str:
        k = self.longest_prefix_palindrome(s)
        s_copy = s

        for i in range(k, len(s)):
            s_copy = s[i] + s_copy
            
        return s_copy
            

        
        
