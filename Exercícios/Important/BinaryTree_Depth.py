class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root, depth):
            if not root: return depth

            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))

        return dfs(root, 0)