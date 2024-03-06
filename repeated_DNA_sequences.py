from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10
        substring_count = defaultdict(int)
        ans = []

        next_substring = s[:k]
        substring_count[next_substring] = 1

        for i in range(1, len(s) - k + 1):
            next_substring = next_substring[1:] + s[i + k - 1]
            substring_count[next_substring] += 1

            if substring_count[next_substring] == 2:
                ans.append(next_substring) 

        return ans
