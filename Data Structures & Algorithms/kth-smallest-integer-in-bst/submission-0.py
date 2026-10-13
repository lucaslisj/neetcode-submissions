# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = []

        def get_list(root):
            if root.left:
                get_list(root.left)
            ans.append(root.val)
            if root.right:
                get_list(root.right)
            return

        get_list(root)
        return ans[k - 1]

        