class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def remove(self, word):
        self._remove_recursive(self.root, word, 0)

    def _remove_recursive(self, node, word, index):
        if index == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
            return

        char = word[index]
        if char not in node.children:
            return

        next_node = node.children[char]
        self._remove_recursive(next_node, word, index + 1)

        if not next_node.children and not next_node.is_end_of_word:
            del node.children[char]

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        res = set()
        prefix = ''

        def explore(prefix, i, j, trie_node):

            if board[i][j] == '#':
                return

            for char in trie_node.children:
                node = trie_node.children[char]
                if node.is_end_of_word and board[i][j] == char:
                    res.add(prefix + char)
                if board[i][j] != char:
                    continue
                else:                 
                    if i-1 >= 0:
                        board[i][j] = '#'
                        explore(prefix + char, i-1, j, node)
                        board[i][j] = char              
                    if i+1 < m:
                        board[i][j] = '#'
                        explore(prefix + char, i+1, j, node)
                        board[i][j] = char
                    if j-1 >= 0:
                        board[i][j] = '#'
                        explore(prefix + char, i, j-1, node)
                        board[i][j] = char
                    if j+1 < n:
                        board[i][j] = '#'
                        explore(prefix + char, i, j+1, node)
                        board[i][j] = char       
            
        trie = Trie()

        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                explore('', i, j, trie.root)
                for word in res:
                    trie.remove(word)

        return res
        







