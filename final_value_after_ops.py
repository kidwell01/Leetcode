class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for op in operations:
            if op == "--X" or op == "X--":
                x -= 1
            elif op == "X++" or op == "++X":
                x += 1
        return x


solution = Solution()
print(solution.finalValueAfterOperations(["++X", "X++"]))
