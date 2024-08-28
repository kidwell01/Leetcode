class Solution(object):
    def findWordsContaining(self, words, x):
        indices = []
        for i in range(len(words)):
            if x in words[i]:
                indices.append(i)
        return indices


solution = Solution()
print(solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))
