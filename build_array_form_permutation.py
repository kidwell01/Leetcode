class Solution(object):
    def buildArray(self, nums):
        ans = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans


solution = Solution()
print(solution.buildArray([5, 0, 1, 2, 3, 4]))

