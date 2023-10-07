class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]
        fruit_pairs = [[] for _ in range(n)]
        dp1[0] = dp2[0] = 1
        fruit_pairs[0]= [fruits[0]]

        for i in range(1, n):
            if fruits[i] == fruits[i - 1]:
                dp1[i] = dp1[i - 1] + 1
                dp2[i] = dp2[i - 1] + 1
                fruit_pairs[i] = fruit_pairs[i - 1]
            else:
                dp1[i] = 1
                if fruits[i] in fruit_pairs[i-1]:
                    dp2[i] = dp2[i - 1] + 1
                    fruit_pairs[i] = fruit_pairs[i - 1]
                else:
                    dp2[i] = dp1[i - 1] + 1
                    fruit_pairs[i] = [fruits[i-1], fruits[i]]

        return max(dp2)  
        
        
