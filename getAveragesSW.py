class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        averages = [-1]*n
        window_size = k*2+1
        
        prefix = [nums[0]]
        
        for i in range(1,n):
            prefix.append(nums[i]+prefix[-1])
            

        for i in range(k,n-k):
            leftbound, rightbound = i - k, i + k
            sumsubarray = prefix[rightbound] - prefix[leftbound] + nums[leftbound]
            averages[i] = sumsubarray // window_size
        return averages
        
