class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        # Store matching opening brackets for each closing bracket
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            # If it is an opening bracket
            if char not in pairs:
                stack.append(char)

            # If it is a closing bracket
            else:

                # No opening bracket available
                if not stack:
                    return False

                # Check whether the top opening bracket matches
                if stack[-1] == pairs[char]:
                    stack.pop()

                else:
                    return False

        # All brackets must be closed
        return len(stack) == 0