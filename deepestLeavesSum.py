from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            curSum = 0
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                curSum += node.val
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
        return curSum
