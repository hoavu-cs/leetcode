class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s) - 1
        output_rows = [[] for i in range(numRows)]
        for i, c in enumerate(s):
            q = i // (numRows - 1)
            r = i - q * (numRows - 1)
            if q % 2 == 0:
                output_rows[r].append(c)
            else:
                output_rows[numRows - r - 1].append(c)
        output = ''.join([''.join(output_rows[i]) for i in range(numRows)])
        return output

        
