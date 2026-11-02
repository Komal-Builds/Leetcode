class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] == pairs[char]:
                    stack.pop()
                else: 
                    return False    
        return len(stack) == 0               