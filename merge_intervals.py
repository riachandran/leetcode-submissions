class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        mergedIntervals = []
        
        for interval in intervals:
            if not mergedIntervals or interval[0] > mergedIntervals[-1][1]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(interval[1], mergedIntervals[-1][1])
        
        return mergedIntervals
