from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        cols = defaultdict(list)
        queue = deque([(root,0)])

        while queue:
            node, col = queue.popleft()
            if node:
                cols[col].append(node.val)
                if node.left:
                    queue.append((node.left,col - 1))
                if node.right:
                    queue.append((node.right,col+1))
            
        
        sorted_cols = sorted(cols.keys())
        return [cols[col] for col in sorted_cols]
