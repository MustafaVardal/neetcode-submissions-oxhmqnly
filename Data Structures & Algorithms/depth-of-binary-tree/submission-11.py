# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, ab):
            if not root:
                return ab
            left = dfs(root.left, ab + 1)
            right = dfs(root.right, ab + 1)

            return max(left, right)

        return dfs(root, 0)
