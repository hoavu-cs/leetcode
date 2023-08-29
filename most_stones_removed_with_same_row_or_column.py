class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        n = len(stones)
        visited = {(s[0], s[1]): False for s in stones}
        tuple_stones = [(s[0], s[1]) for s in stones]
        stones = tuple_stones
        row_coordinates = {}
        col_coordinates = {}

        # preprocess: sort two coordinates for faster DFS
        for x in stones:
            if x[0] in row_coordinates:
                row_coordinates[x[0]].append(x)
            else:
                row_coordinates[x[0]] = [x]

            if x[1] in col_coordinates:
                col_coordinates[x[1]].append(x)
            else:
                col_coordinates[x[1]] = [x] 

        def explore(x):
            nonlocal visited
            visited[x] = True
            for y in row_coordinates[x[0]]:
                if not visited[y]:
                    explore(y)
            for y in col_coordinates[x[1]]:
                if not visited[y]:
                    explore(y)

        number_of_components = 0
        for x in stones:
            if not visited[x]:
                explore(x)
                number_of_components += 1
        
        return len(stones) - number_of_components
