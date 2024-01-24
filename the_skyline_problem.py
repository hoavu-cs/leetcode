from heapq import heappush, heappop
from math import inf

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points, active, output, S = [], [], [], []

        for p in buildings:
            left, right, height = p
            points.append((left, right, height))
            points.append((right, -1, height))

        points.sort(key = lambda x: (x[0], x[1], -x[2]))

        for p in points:
            a, b, height = p
            
            if b != -1:
                # see a left edge
                while len(active) > 0 and active[0][1] < a:
                    heappop(active)

                if (len(active) > 0 and height > -active[0][0]) or (len(active) == 0):
                    S.append([a, height, True, 0])

                heappush(active, (-height, b))
            else:
                # see a right edge
                while len(active) > 0 and active[0][1] <= a:
                    heappop(active)

                if (len(active) > 0 and height > -active[0][0]):
                    S.append([a, -active[0][0], False, 0])
                elif len(active) == 0:
                    S.append([a, 0, False, height])

        # handle the cases where x-coordinates of keypoints are equal
        i = 0
        while i < len(S):
            j = i
            has_left = False
            max_left_height, max_right_height = -inf, -inf

            while j < len(S) and S[i][0] == S[j][0]:
                if S[j][2]:
                    has_left = True
                    max_left_height = max(max_left_height, S[j][1])
                else:
                    max_right_height = max(max_right_height, S[j][1], S[j][3])
                j += 1 
                
            if not has_left:
                output.append([S[i][0], S[i][1]])
            elif max_left_height != max_right_height and has_left:
                output.append([S[i][0], max_left_height])
            
            i = j

        return output



                
                



