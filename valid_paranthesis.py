class Solution(object):
    def isValid(self, s):
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        valid = True
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if len(stack) != 0:
                    top = stack.pop()
                    if char != brackets[top]:
                        valid = False
                        break
                    else:
                        valid = True
                else:
                    valid = False
                    break

        if len(stack) != 0:
            valid = False

        return valid

solution = Solution()
print(solution.isValid("["))