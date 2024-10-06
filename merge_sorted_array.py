class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
        return nums1


solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))