from collections import defaultdict

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        required = defaultdict(int)
        char_count = defaultdict(int)
        i, j, min_j = 0, 0, 0

        for c in t:
            required[c] += 1
        
        total = 0
        while i < m:
            if s[i] in required:
                char_count[s[i]] += 1
                if char_count[s[i]] == required[s[i]]:
                    total += char_count[s[i]]
                    if total == len(t):
                        break
            i += 1

        if i == m: return ''

        min_i = i
        while i < m:
            while j <= i:
                if s[j] in required:
                    char_count[s[j]] -= 1
                    removed_char = s[j]
                    if char_count[s[j]] < required[s[j]]:
                        j += 1
                        break
                j += 1

            if i - (j - 1) < min_i - min_j:
                min_i, min_j = i, j - 1

            i += 1
            while i < m:
                if s[i] in required:
                    char_count[s[i]] += 1
                    if s[i] == removed_char:
                        break
                i += 1

        return s[min_j : min_i + 1]
