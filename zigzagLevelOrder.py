from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        even_level = False
        ans =[]
        while queue:
            length = len(queue)
            temp = deque()
            for _ in range(length):
                node = queue.popleft()
                if even_level:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
            ans.append(list(temp))
            even_level = not even_level
        return ans
