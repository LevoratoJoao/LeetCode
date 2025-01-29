# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> list[int]:
        result = []
        def dfs(root):
            if root == None:
                return None
            nonlocal result
            self.inorderTraversal(root.left)
            result.append(root.val)
            self.inorderTraversal(root.right)
            return result
        dfs(root)
        return result

sol = Solution()
sol.inorderTraversal([1,None,2,3])