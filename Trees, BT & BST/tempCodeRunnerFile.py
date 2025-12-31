class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def dfs(root, curr_sum):
            if not root:
                return False
            curr_sum += root.val
            if not root.left and not root.right:
                return curr_sum == targetSum
            return dfs(root.left, curr_sum) or dfs(root.right,curr_sum)
        return dfs(root,0)