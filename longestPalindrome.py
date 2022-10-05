class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start = end = 0
        length = len(s)
        for i in range(length):
            print('i: '+str(i))
            max_len_1 = self.get_max_len(s, i, i + 1)
            max_len_2 = self.get_max_len(s, i, i)
            max_len = max(max_len_1, max_len_2)
            print('in for')
            print(max_len_1,max_len_2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
            print('string: '+s[start: end+1])
        return s[start: end+1]
        
    def get_max_len(self, s: 'list', left: 'int', right: 'int') -> 'int':
        length = len(s)
        i = 1
        max_len = 0
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
            print('in while')
            print(left,right)
            print(s[left:right])
        return right - left - 1
