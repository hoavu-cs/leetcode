class Solution:

    def __init__(self):
        self.mult_table = {}

    def compute_mult_table(self, num):
        n = len(num)
        self.mult_table[num] = set()

        if n == 1:
            self.mult_table[num].add((int(num), str(num)))
        elif n == 0:
            self.mult_table[num].add((1, '1'))
        else:
            if num[0] != '0':
                self.mult_table[num].add((int(num), str(num)))

            for i in range(1, n):
                left = num[:i]
                right = num[i:]
                if left not in self.mult_table:
                    self.compute_mult_table(left)
                if right not in self.mult_table:
                    self.compute_mult_table(right)
                for x, x_expression in self.mult_table[left]:
                    for y, y_expression in self.mult_table[right]:
                        self.mult_table[num].add((x * y, x_expression + '*' +  y_expression))

    def search(self, num, target):
        n = len (num)
        ans = [] 

        # case 1: no + or - will be inserted
        for x, x_expression in self.mult_table[num]:
            if x == target:
                ans.append(x_expression)
        
        # case 2: insert at least one + or -
        for i in range(1, n):
            left = num[:i]
            right = num[i:]
            for x, x_expression in self.mult_table[left]:
                # search for possibilities of left + right
                remaining_target = target - x
                R = self.search(right, remaining_target)
                for y_expression in R:
                    ans.append(x_expression + '+' + y_expression)
                # search for possibilities of left - right
                remaining_target = x - target
                R = self.search(right, remaining_target)
                for y_expression in R:
                    trans_table = str.maketrans("+-", "-+")
                    y_expression = y_expression.translate(trans_table)
                    ans.append(x_expression + '-' + y_expression)
        return ans

    def addOperators(self, num: str, target: int) -> List[str]:

        self.compute_mult_table(num)
        ans = self.search(num, target)
        return ans
 
        
