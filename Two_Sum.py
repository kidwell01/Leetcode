class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    indices.append(i)
                    indices.append(j)

        return indices
solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
