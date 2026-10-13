# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# brute force
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        
        max_allowed = {} # key is node, val is max allowed
        min_allowed = {} # key is node, val is min allowed

        max_allowed[root] = 1000000001
        min_allowed[root] = -1000000001

        queue = collections.deque()
        queue.append(root)

        while queue:
            cur = queue.popleft()
            if cur.val >= max_allowed[cur] or cur.val <= min_allowed[cur]:
                return False
            if cur.left:
                queue.append(cur.left)
                max_allowed[cur.left] = cur.val
                min_allowed[cur.left] = min_allowed[cur]
            if cur.right:
                queue.append(cur.right)
                max_allowed[cur.right] = max_allowed[cur]
                min_allowed[cur.right] = cur.val
            
        return True
        

        
        