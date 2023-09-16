class Solution:
  
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      
        def custom_key(x):
            t = 0 if x[1] == 'beginning' else 1
            return x[0], t

        n = len(intervals)
        end_points = [(intervals[i][0], 'beginning') for i in range(n)]
        end_points += [(intervals[i][1], 'ending') for i in range(n)]
        end_points = sorted(end_points, key=custom_key)
        res = []
        stack = []

        next_begin = end_points[0][0]
        new_interval = False

        for x in end_points:
            if new_interval:
                next_begin = x[0]
                new_interval = False

            if x[1] == 'ending':
                stack.pop()
            else:
                stack.append(x[0])

            if not stack:
                res.append([next_begin, x[0]]) 
                new_interval = True

        return res
