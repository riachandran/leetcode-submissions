class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_bracket = ["(", "[", "{"]
        stack = [] 
        for i in s:
            if i in open_bracket:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return len(stack) == 0
