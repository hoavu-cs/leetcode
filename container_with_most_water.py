class Solution:
    def maxAreaWithHigherLeftLine(self, height):
        # find the largest area where the left line >= the right line (and vice versa)
        # n: number of input lines
        # running time: O(n log n)
        height_set = sorted(list(set(height)))
        highest_so_far = height[0]
        cur = bisect_left(height_set, highest_so_far)+1
        F = {} # F[v] contains the first index whose height is at least v
        n = len(height)
        largest = 0 # contains the largest area using line i on the right

        for v in range(height[0]+1):
            F[v] = 0
        
        for i in range(1, n):
            if height[i] > highest_so_far:
                next_cur = bisect_left(height_set, height[i])+1
                highest_so_far = height[i]
                for k in range(cur, next_cur):
                    F[height_set[k]] = i
                cur = next_cur
            if largest < (i-F[height[i]])*height[i]: largest = (i-F[height[i]])*height[i]
        
        return largest

    def maxArea(self, height: List[int]) -> int:
        reverse_height = list(reversed(height))
        return max(self.maxAreaWithHigherLeftLine(height), self.maxAreaWithHigherLeftLine(reverse_height))
        