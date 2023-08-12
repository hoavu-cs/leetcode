class Solution:

    def indexWordSquares(self, words: List[str]) -> List[List[str]]:
        output = []
        smaller_words = []
        string_loc = {}

        if len(words[0]) == 1:
            return [[i] for i in range(len(words))] 

        for i, s in enumerate(words):
            smaller_words.append(s[1:])
            if s[1:] not in string_loc:
                string_loc[s[1:]] = [i]
            else:
                string_loc[s[1:]].append(i)

        L = self.indexWordSquares(smaller_words)

        for square in L:
            first_column = ""
            for i in square:
                first_column += words[i][0]

            if first_column in string_loc:
                for j in string_loc[first_column]:
                    larger_square = square[:]
                    larger_square.insert(0, j)
                    output.append(larger_square)

        return output

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        squares_by_indices = self.indexWordSquares(words)
        squares = [[words[i] for i in x] for x in squares_by_indices]

        return squares

