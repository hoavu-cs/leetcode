class Solution:
    def findStrobogrammaticWithLeadingZeros(self, n: int) -> List[str]:
        if n == 1:
            return ['0', '1', '8']
        elif n == 2:
            return ['00', '11', '69', '88', '96']
        else:
            output = []
            S = self.findStrobogrammaticWithLeadingZeros(n-2)
            for s in S:
                output.append('0' + s + '0')
                output.append('1' + s + '1')
                output.append('8' + s + '8')
                output.append('6' + s + '9')
                output.append('9' + s + '6')
            return output

    def findStrobogrammatic(self, n: int) -> List[str]:
        S = self.findStrobogrammaticWithLeadingZeros(n)
        output = []
        for s in S:
            if n == 1:
                output.append(s)
            elif n > 1 and s[0] != '0':
                output.append(s) 
        return output

