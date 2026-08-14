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
        
        que = deque([root])
        res = []
        while que:
            level_size = len(que)
            curr_level = []
            for _ in range(level_size):
                node = que.popleft()
                curr_level.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(curr_level)
            
        
        return res