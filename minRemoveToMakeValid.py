class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        str_list = list(s)
        for i in range(len(str_list)):
            if str_list[i] == '(': stack.append([i,str_list[i]])
            elif str_list[i] == ')':
                if stack == [] or stack[-1][1] == ')': stack.append([i,str_list[i]])
                elif stack[-1][1] == '(' : stack.pop(-1)

        if stack != []:
            for i in range(len(stack)):
                str_list[stack[i][0]] = ""
        return ''.join(str_list)
