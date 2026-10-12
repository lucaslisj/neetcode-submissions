# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = []
        queue.append(root)
    
        height = {} # key is the node, val is its height
        height_lists = {} # key is height, value is a list of node values with that height

        height[root] = 0
        max_height = 0

        while queue:
            cur = queue.pop(0)
            cur_height = height[cur]
            max_height = max(max_height, cur_height)
            height_lists[cur_height] = height_lists.get(cur_height,[]) + [cur.val]

            if cur.left:
                queue.append(cur.left)
                height[cur.left] = cur_height + 1
                
            if cur.right:
                queue.append(cur.right)
                height[cur.right] = cur_height + 1
        
        for i in range(max_height + 1):
            ans.append(height_lists[i])
        return ans



