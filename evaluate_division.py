
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        nodes = set()
        table = {}
        ans = []

        for u, v in equations:
            nodes.add(u)
            nodes.add(v)
            table[(u, u)] = table[(v, v)] = 1

        adj_list = {u: [] for u in nodes}

        for i, (u, v) in enumerate(equations):
            adj_list[u].append((v, values[i]))
            adj_list[v].append((u, 1/values[i]))
        
        for u, v in queries:
            if u not in nodes or v not in nodes:
                ans.append(-1)
                continue 
            if (u, v) in table:
                ans.append(table[(u, v)])
                continue

            queue = [u]
            explored = set()
            stop_bfs = False
            while len(queue) > 0:
                a = queue.pop(0)
                for b, weight in adj_list[a]:
                    if b not in explored:
                        table[(u, b)] = table[(u, a)] * weight
                        queue.append(b)
                    if b == v:
                        stop_bfs = True
                if stop_bfs:
                    break
                explored.add(a)
            if (u, v) in table:
                ans.append(table[(u, v)])
            else:
                ans.append(-1)
                
        return ans


                

        

    