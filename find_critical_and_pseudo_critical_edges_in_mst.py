from math import inf

class Solution:

    def dfs(self, u, adj_list, visited):
        visited[u] = True
        for v, weight in adj_list[u]:
            if not visited[v]:
                self.dfs(v, adj_list, visited)

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = [[] for v in range(n)]
        edge_idx = {}
        critical, pseudo_critical = set(), set()

        for idx, e in enumerate(edges):
            u, v, weight = e
            edge_idx[(u, v)] = edge_idx[(v, u)] = idx

            adj_list[u].append((v, weight))
            adj_list[v].append((u, weight))

        T = set()
        T_edges = []
        T.add(0)

        # Prim's
        while len(T) < n:
            min_weight = inf
            inside_node = None
            next_node = None

            for u in T:
                for v, weight in adj_list[u]:
                    if v not in T and weight < min_weight:
                        min_weight = weight
                        inside_node = u
                        next_node = v
            T.add(next_node)
            T_edges.append(edge_idx[(inside_node, next_node)])

        adj_list_T = [set() for v in range(n)]

        for idx in T_edges:
            u, v, weight = edges[idx]
            adj_list_T[u].add((v, weight))
            adj_list_T[v].add((u, weight))

        for idx in T_edges:
            u, v, weight = edges[idx]
            adj_list_T[u].remove((v, weight))
            adj_list_T[v].remove((u, weight))
            visited = [False for i in range(n)]
            is_critical = True

            self.dfs(u, adj_list_T, visited)

            for a, b, weight2 in edges:
                if (visited[a] != visited[b]) and weight2 == weight and ((a not in [u, v]) or (b not in [u, v])):
                    pseudo_critical.add(edge_idx[(a, b)])
                    pseudo_critical.add(edge_idx[(u, v)])
                    is_critical = False
                
            if is_critical:
                critical.add(edge_idx[(u, v)])

            adj_list_T[u].add((v, weight))
            adj_list_T[v].add((u, weight))

        return [list(critical), list(pseudo_critical)]


                    
