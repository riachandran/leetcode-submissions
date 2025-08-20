class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = [char for char in s if char.isalpha()]
        left = 0
        n = len(s)
        right = n - 1
        pointer = len(arr) - 1
        revarr = []

        while left < n:
            if s[left].isalpha():
                revarr.append(arr[pointer])
                right -= 1
                pointer -= 1

            elif not s[left].isalpha():
                revarr.append(s[left])

            left += 1

        return "".join(revarr)
