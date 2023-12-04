class Solution:

    def dfs(self, adj_list, source):
        ret = [source]
        dead_end = []
        
        if len(adj_list[source]) == 0:
            return ret

        v = adj_list[source][0]
        adj_list[source].pop(0)
        recursive_itinerary = self.dfs(adj_list, v)

        if len(adj_list[source]) > 0:
            dead_end = recursive_itinerary
            v = adj_list[source][0]
            adj_list[source].pop(0)
            recursive_itinerary = self.dfs(adj_list, v)

        ret = ret + recursive_itinerary + dead_end
        return ret

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airports = set(_[0] for _ in tickets)
        airports = airports.union(set(_[1] for _ in tickets))

        adj_list = {_ : [] for _ in airports}

        for ticket in tickets:
            adj_list[ticket[0]].append(ticket[1])
        
        for airport in adj_list:
            adj_list[airport].sort()

        return self.dfs(adj_list, 'JFK')
