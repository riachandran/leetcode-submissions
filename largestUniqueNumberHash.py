from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen = set()
        unseen = set()
        for num in nums:
            if num not in unseen and num not in seen: unseen.add(num)
            elif num in unseen:
                seen.add(num)
                unseen.remove(num)

        return max(unseen) if len(unseen)!= 0 else -1
