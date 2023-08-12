class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct the graph
        n, m = numCourses, len(prerequisites)
        adj_list = {i: [] for i in range(n)}
        in_degree = {i: 0 for i in range(n)}
        removed = set()
        res = []

        # adjacency list of v holds all outgoing edges toward v
        for e in prerequisites:
            adj_list[e[1]].append(e[0])
            in_degree[e[0]] += 1

        next_course = []
        for i in range(n):
            if in_degree[i] == 0:
                next_course.append(i)
            
        while len(next_course) > 0:
            i = next_course[0]
            next_course.pop(0)
            removed.add(i)
            res.append(i)
            for j in adj_list[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0 and j not in removed:
                    next_course.append(j)

        if len(res) < n:
            return []
        else:
            return res
            

        


