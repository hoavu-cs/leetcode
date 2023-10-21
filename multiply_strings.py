class Solution:

    def subtract_strings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1  
        borrow = 0  
        result = []  
                
        while i >= 0 or j >= 0 or borrow:
            digit1 = int(num1[i]) if i >= 0 else 0  
            digit2 = int(num2[j]) if j >= 0 else 0  
            total = digit1 - digit2 - borrow

            if total < 0:
                total += 10
                borrow = 1
            else:
                borrow = 0
            
            result.append(str(total)) 
            i, j = i - 1, j - 1  
        result_str = ''.join(reversed(result)).lstrip("0")
        return result_str if result_str else '0'

    def add_strings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1  
        carry = 0  
        result = []  
        
        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0  
            digit2 = int(num2[j]) if j >= 0 else 0  
            
            total = digit1 + digit2 + carry  
            
            carry = total // 10 
            result.append(str(total % 10)) 
            
            i, j = i - 1, j - 1  
        
        return ''.join(reversed(result)) 

    def multiply(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        if n <= 2:
            return str(int(num1)*int(num2))
        while len(num1) < n:
            num1 = '0' + num1
        while len(num2) < n:
            num2 = '0' + num2
        m = n // 2
        x0, y0 = num1[m:], num2[m:]
        x1, y1 = num1[:m], num2[:m]

        z2 = self.multiply(x1, y1)
        z0 = self.multiply(x0, y0)
        t = self.multiply(self.add_strings(x1, x0), self.add_strings(y1, y0))

        t = self.subtract_strings(t, z0)
        t = self.subtract_strings(t, z2)
        z1 = t

        k = n - m

        z2 += '0' * (2*k)
        z1 += '0' * k

        res = self.add_strings(z1, z2)
        res = self.add_strings(res, z0)

        while len(res) > 1 and res[0] == '0':
            res = res[1:]

        return res
            
