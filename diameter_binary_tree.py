class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def cal(node):
            # print(node)
            if not node:
                return 0
            nonlocal diameter
            
            leftpath = cal(node.left)
            rightpath = cal(node.right)
            
            diameter = max(diameter,leftpath+rightpath)
            
            return max(leftpath,rightpath)+1
        
        cal(root)
        return diameter
