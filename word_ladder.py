from math import inf
from itertools import combinations

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = []
        adj_list = {}
        dist = {}

        if endWord not in wordList:
            return 0

        # build a graph
        if beginWord in wordList:
            nodes = wordList
        else:
            nodes = [beginWord] + wordList

        adj_list = {word: [] for word in nodes}

        for i in range(len(beginWord)):
            remove_i_list = [word[:i] + word[i+1:] for word in nodes]
            index_table = {}
            for j, word in enumerate(remove_i_list):
                if word in index_table:
                    index_table[word].append(j)
                else:
                    index_table[word] = [j]
            for word in index_table:
                for u, v in combinations(index_table[word], 2):
                    adj_list[nodes[u]].append(nodes[v])
                    adj_list[nodes[v]].append(nodes[u])
        
        dist = {word: inf for word in nodes}
        dist[beginWord] = 0
        
        # bfs from beginWord
        queue.append(beginWord)

        while len(queue) > 0:
            u = queue[0]
            del queue[0]
            for v in adj_list[u]: 
                if dist[v] == inf and sum([c1 != c2 for c1, c2 in zip(u, v)]) == 1:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        return dist[endWord] + 1 if dist[endWord] != inf else 0
