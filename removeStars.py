class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter == "*":
                if stack: 
                    stack.pop()
                    continue
            else:
                stack.append(letter)

        return "".join(stack)   
