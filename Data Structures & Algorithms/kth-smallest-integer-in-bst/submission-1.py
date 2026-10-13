# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = 0
        count = k
        flag = 1
        
        def dfs(root):
            nonlocal ans, k, flag
            if flag == 0:
                return
            if root.left:
                dfs(root.left)
            k -= 1
            if k == 0:
                ans = root.val
                flag = 0
            if root.right:
                dfs(root.right)

        dfs(root)
        return ans