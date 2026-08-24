class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in pairs:
                # Closing bracket
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

            else:
                # Opening bracket
                stack.append(char)

        return len(stack) == 0