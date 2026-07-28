# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal = float('-inf')
        

        def dfs(root):
            
            if not root:
                return 0
            left = max(dfs(root.left), 0)
            right= max(dfs(root.right), 0)

            curr_path = root.val + left + right
            self.maxVal = max(self.maxVal, curr_path)
            return root.val + max(left, right)
        dfs(root)
        return self.maxVal

