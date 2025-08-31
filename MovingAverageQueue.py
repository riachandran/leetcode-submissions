class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.output = []
        self.curSum = 0
    def next(self, val: int) -> float:
        if len(self.output) == self.size:
            element = self.output.pop(0)
            self.output.append(val)
            self.curSum -= element
            self.curSum += val
        else:
            self.curSum += val
            self.output.append(val)
            
        return self.curSum/len(self.output)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
