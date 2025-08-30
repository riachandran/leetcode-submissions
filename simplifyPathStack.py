class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p= [word for word in path.split('/')]
        print(p)
        for i in range(1,len(p)):
            if p[i] == '..':
                if len(stack) >= 1: 
                    stack.pop(-1)
                    continue
            elif p[i] == '' or p[i] == '.': continue
            else: stack.append('/'+p[i])

        if stack == []: return '/'
        return "".join(stack)
