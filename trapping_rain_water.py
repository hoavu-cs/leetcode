class Solution:

    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_vol = 0
        highest_from_right = [0 for i in range(n)]
        highest_so_far = 0

        # compute the highest point among height[i...n-1] for each i
        for i in range(n-1, -1, -1):
            highest_from_right[i] = highest_so_far = max(highest_so_far, height[i])  
        i = 0

        while i < n-1:
            j = i+1
            next_vol = 0
            # compute the water trap between i and the next check point
            if highest_from_right[i+1] >= height[i]: 
                # case 1: the next check point is at least as high than the current check point
                while height[j] < height[i]:
                    next_vol += height[i]-height[j]
                    j += 1
                i = j
            else:
                # case 2: the next check point is lower than the current check point
                while height[j] < highest_from_right[i+1]:
                    next_vol += highest_from_right[i+1]-height[j]
                    j += 1
                i = j
            total_vol += next_vol
        return total_vol
            
            

