class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for letter in s:
            if len(stack) > 0:
                if letter.lower() == stack[-1].lower() and letter != stack[-1]:
                    stack.pop()
                    continue       
            stack.append(letter)
                
        return ''.join(stack)
