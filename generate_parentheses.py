class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        if n == 1:
            return ["()"]
        else:
            L = self.generateParenthesis(n-1)
            valid_table = {}
            for s in L:
                for i in range(len(s)):
                    for j in range(i, len(s)):
                        candidate = s[:i]+ '(' + s[i: j] + ')' + s[j:]
                        if candidate not in res:
                            res.add(candidate)
            return list(res)
