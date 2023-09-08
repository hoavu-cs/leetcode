class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(s)
        m = len(indices)
        
        replacements = list(zip(indices, sources, targets))
        sorted_replacements = sorted(replacements, key=lambda x: x[0])
        indices = [r[0] for r in sorted_replacements]
        sources = [r[1] for r in sorted_replacements]
        targets = [r[2] for r in sorted_replacements]

        occur = [s[indices[i]:].startswith(sources[i]) for i in range(m)]

        res = ''
        pointer = 0
        for i in range(m):
            if occur[i]:
                res += s[pointer:indices[i]] + targets[i]
                pointer = indices[i] + len(sources[i]) 

        res += s[pointer:]
        return res
