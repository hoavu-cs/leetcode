class Solution:
    def is_strechy(self, word, s):
        previous_char = None
        word_groups = []
        s_groups = []
        for char in word:
            if char == previous_char:
                word_groups[-1]['count'] += 1
            else:
                word_groups.append({'char': char, 'count': 1})
            previous_char = char

        previous_char = None
        for char in s:
            if char == previous_char:
                s_groups[-1]['count'] += 1
            else:
                s_groups.append({'char': char, 'count': 1})
            previous_char = char

        if len(s_groups) != len(word_groups):
            return False
        else:
            for idx in range(len(s_groups)):
                if (s_groups[idx]['count'] < word_groups[idx]['count']) \
                or (s_groups[idx]['count'] < 3 and s_groups[idx]['count'] > word_groups[idx]['count'])\
                or (s_groups[idx]['char'] != word_groups[idx]['char']):
                    return False
            return True
                    
    def expressiveWords(self, s: str, words: List[str]) -> int:
        result = 0
        for word in words:
            if self.is_strechy(word, s):
                print(word, s)
                result += 1

        return result


        
