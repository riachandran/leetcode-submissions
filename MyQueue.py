class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        return self.queue

    def pop(self) -> int:
        element = self.queue.pop(0)
        return element

    def peek(self) -> int:
        element = self.queue[0]
        return element

    def empty(self) -> bool:
        return self.queue == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
