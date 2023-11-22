from collections import defaultdict
import copy

class Solution:
    def findSubstring(self, s, words):
        word_count = defaultdict(int)
        word_length = len(words[0])
        n = len(s)
        m = len(words)
        ret = []
        
        for w in words:
            word_count[w] += 1

        for l in range(word_length):
            s_offset = s[l:]
            i = 0
            word_count_diff = copy.copy(word_count)

            for j in range(i, word_length * m, word_length):
                word_count_diff[s_offset[j: j + word_length]] -= 1
                if all(value == 0 for value in word_count_diff.values()):
                    ret.append(i + l)
            
            i += word_length

            while i + m * word_length - 1 < len(s_offset):
                removed_word = s_offset[i - word_length: i]
                added_word = s_offset[i + (m - 1) * word_length: i + m * word_length]
                word_count_diff[removed_word] += 1
                word_count_diff[added_word] -= 1

                if all(value == 0 for value in word_count_diff.values()):
                    ret.append(i + l)

                i = i + word_length

        return ret



