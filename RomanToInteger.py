class Solution(object):
    def romanToInt(self, s):
        integers = []
        result = 0
        symbol_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for char in s:
            integers.append(symbol_value[char])
        i = 0
        while i < len(integers) - 1:
            if integers[i] < integers[i+1]:
                result += integers[i+1] - integers[i]
                i += 2
            else:
                result += integers[i]
                i += 1
        if i == len(integers) - 1:
            result += integers[i]
        return result

solution = Solution()
print(solution.romanToInt("II"))