# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        levels = []
        
        def helper(node,level):
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if int(node.left.val) > int(node.right.val):
                return False
            else: 
                print(node.val,node.left.val,node.right.val)
                if node.left:
                    helper(node.left,level+1)
                if node.right:
                    helper(node.right,level+1)
                
                
        helper(root,0)
        return True
        
        
        
