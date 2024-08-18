class Solution(object):
    def searchInsert(self, nums, target):
        index = 0
        # Provided target is in the list
        for index, num in enumerate(nums):
            if num == target:
                return index
        # Provided target is not in the list
        if target not in nums:
            nums.append(target)
            nums.sort()
            print(nums)
            for i in range(len(nums)):
                if nums[i] == target:
                    return i

solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 7))