class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqd = {}
        max_freq = 0

        for num in nums:
            if num in freqd:
                freqd[num] += 1
            else:
                freqd[num] = 1
            max_freq = max(max_freq,freqd[num])

        return sum(freqd[d] for d in freqd if freqd[d] == max_freq)
