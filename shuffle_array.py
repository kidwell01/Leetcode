class Solution(object):
    def shuffle(self, nums, n):
        temp = []
        for i in range(n):
                temp.append(nums[i])
                temp.append(nums[i + n])
        return temp


solution = Solution()
print(solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))

