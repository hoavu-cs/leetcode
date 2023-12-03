class Solution:

    def compute_scramble_dp(self, s1, s2, dp):
        n = len(s1)

        if n == 1:
            dp[(s1, s2)], dp[(s2, s1)]  = (s1 == s2), (s1 == s2)
            return
        elif sorted(s1) != sorted(s2):
            dp[(s1, s2)], dp[(s2, s1)]  = False, False
            return
        elif s1 == s2:
            dp[(s1, s2)], dp[(s2, s1)]  = True, True
            return

        for i in range(1, n):
            left1, right1 = s1[:i], s1[i:]
            left2, right2 = s2[:i], s2[i:]
            left3, right3 = s2[n - i:], s2[:n - i]
            
            if (left1, left2) not in dp and (left2, left1) not in dp:
                self.compute_scramble_dp(left1, left2, dp) 
            if (right1, right2) not in dp and (right2, right1) not in dp:
                self.compute_scramble_dp(right1, right2, dp)
            if dp[(left1, left2)] and dp[(right1, right2)]:
                dp[(s1, s2)], dp[(s2, s1)] = True, True
                return
        
            if (left1, left3) not in dp and (left3, left1) not in dp:
                self.compute_scramble_dp(left1, left3, dp)
            if (right1, right3) not in dp and (right3, right1) not in dp:
                self.compute_scramble_dp(right1, right3, dp)
            if dp[(left1, left3)] and dp[(right1, right3)]:
                dp[(s1, s2)], dp[(s2, s1)]  = True, True
                return
            
        dp[(s1, s2)], dp[(s2, s1)] = False, False

    def isScramble(self, s1: str, s2: str) -> bool:
        dp = {}
        self.compute_scramble_dp(s1, s2, dp)
        return dp[(s1, s2)]






        


         
