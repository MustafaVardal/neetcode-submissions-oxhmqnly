class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        right, left = root.left, root.right
        root.left = self.invertTree(left)
        root.right = self.invertTree(right)

        return root