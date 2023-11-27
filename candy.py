class Solution:

    def candy(self, ratings):
        if len(ratings) == 1:
            return 1
        elif len(ratings) == 0:
            return 0

        n = len(ratings)
        ans = 0
        candies = [1 for i in range(n)]

        for i in range(1, n - 1):
            if ratings[i] > ratings[i - 1] and ratings[i] < ratings[i + 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and ratings[i] < ratings[i - 1]:
                candies[i] = candies[i + 1] + 1

        for i in range(1, n - 1):
            if ratings[i] >= ratings[i - 1] or ratings[i] >= ratings[i + 1]:
                left, right = 0, 0
                if ratings[i] > ratings[i - 1]:
                    left = candies[i - 1]
                if ratings[i] > ratings[i + 1]:
                    right = candies[i + 1]
                candies[i] = max(left, right) + 1

        if ratings[0] > ratings[1]:
            candies[0] = candies[1] + 1
        if ratings[n - 1] > ratings[n - 2]:
            candies[n - 1] = candies[n - 2] + 1

        return sum(candies)
