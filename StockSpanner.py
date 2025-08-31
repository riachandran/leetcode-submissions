class StockSpanner:

    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        stack = self.stack

        curr_price, span = price, 1
        while stack and stack[-1][0] <= curr_price:
            prev_price, prev_span = stack.pop()
            span += prev_span

        stack.append((curr_price,span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
