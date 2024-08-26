class Solution(object):
    def numIdenticalPairs(self, nums):
        good_pairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
        return good_pairs


solution = Solution()
print(solution.numIdenticalPairs([1, 1, 1, 1]))