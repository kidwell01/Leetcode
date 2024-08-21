class Solution(object):
    def minimumOperations(self, nums):

        min_num_of_ops = 0
        for num in nums:
            while num % 3 != 0:
                if num < 2:
                    num -= 1
                    min_num_of_ops += 1
                elif (num + 1) % 3 == 0:
                    num += 1
                    min_num_of_ops += 1
                else:
                    num -= 1
                    min_num_of_ops += 1

        return min_num_of_ops


solution = Solution()
print(solution.minimumOperations([1, 2, 3, 4]))