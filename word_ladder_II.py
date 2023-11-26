from collections import defaultdict
from math import inf

class Solution:

    def construct_path(self, previous, destination):
        if previous[destination] == None:
            return [[destination]]
        else:
            ans = []
            for p in previous[destination]:
                paths = self.construct_path(previous, p)
                for path in paths:
                    ans.append(path + [destination])
            return ans

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        queue = [beginWord]
        adj_list = {}
        previous = {}
        dist = defaultdict(int)
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return []

        for word in wordList:
            dist[word] = inf
            previous[word] = set()
            adj_list[word] = set()
        dist[beginWord] = 0
        previous[beginWord] = None

        for i in range(len(beginWord)):
            remove_i_list = [word[:i] + word[i+1:] for word in wordList]
            index_table = {x: [] for x in remove_i_list}
            for j, x in enumerate(remove_i_list):
                index_table[x].append(j)
            for x in index_table:
                for u, v in combinations(index_table[x], 2):
                    adj_list[wordList[u]].add(wordList[v])
                    adj_list[wordList[v]].add(wordList[u])
        
        while len(queue) > 0:
            word = queue.pop(0)
            for word2 in adj_list[word]:
                if dist[word2] == inf:
                    dist[word2] = dist[word] + 1
                    previous[word2].add(word)
                    queue.append(word2)
                elif dist[word2] == dist[word] + 1:
                    previous[word2].add(word)
                if dist[word2] > dist[endWord]:
                    break

        return self.construct_path(previous, endWord)
