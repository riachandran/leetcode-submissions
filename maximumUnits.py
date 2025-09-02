class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        output = 0
        curr = 0
        boxTypes = sorted(boxTypes,key=lambda x: x[1],reverse=True)
        for count,unit in boxTypes:
            if curr+count <= truckSize:
                output += count*unit
                curr += count
            else:
                output += (truckSize - curr)*unit
                break
        return output
