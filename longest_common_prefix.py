class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return 0
        min_length = min([len(s) for s in strs])
        mismatch = False
        i = 0
        while i < min_length and not mismatch:
            next_char = strs[0][i]
            for s in strs:
                if s[i] != next_char: mismatch = True
            i += 1
        if mismatch:
            return strs[0][:i-1]
        else:
            return strs[0][:min_length]