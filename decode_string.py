class Solution:
    def decodeString(self, s: str) -> str:
        output = ''
        while len(s) > 0:
            i = 0
            text = ''
            while i < len(s) and not s[i].isdigit():
                text += s[i]
                i += 1
            output += text
            if i == len(s):
                return output
            else:
                number = '0'
                while s[i].isdigit():
                    number += s[i]
                    i += 1
                number = int(number)
                j = i + 1
                counter = 1
                while counter > 0:
                    if s[j] == '[': counter += 1
                    if s[j] == ']': counter -= 1
                    j += 1
                output += number*self.decodeString(s[i+1:j-1])
                s = s[j:]
        return output
