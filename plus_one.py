class Solution(object):
    def plusOne(self, digits):
        large_int = int(''.join(map(str, digits)))
        large_int += 1
        result = []

        for i in str(large_int):
            result.append(i)
        int_result = list(map(int, result))
        return int_result


solution = Solution()
print(solution.plusOne([1, 2, 4, 4]))