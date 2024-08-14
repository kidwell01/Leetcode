class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        longest_common_prefix = strs[0]

        for str in strs[1:]:
            while not str.startswith(longest_common_prefix):
                longest_common_prefix = longest_common_prefix[:-1]
                if not longest_common_prefix:
                    return ""
        return longest_common_prefix


solution = Solution()
print(solution.longestCommonPrefix(["Flower", "Flow", "Flight"]))
