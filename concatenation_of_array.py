class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans

# can also use the easy approach by using the extend function
"""
def getConcatenation(self, nums):
    nums.extend(nums)
    return nums
    
    OR
    
    ans = nums + nums
    return ans
"""


solution = Solution()
print(solution.getConcatenation([1, 3, 2, 1]))