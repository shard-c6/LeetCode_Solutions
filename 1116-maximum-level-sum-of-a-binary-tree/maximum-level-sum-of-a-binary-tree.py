# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = deque([root])
        current_level = 1
        max_sum = float('-inf')
        max_level = 1
        
        while queue: 
            level_length = len(queue) 
            
            current_level_sum = 0 
            
            for i in range(level_length): 
                node = queue.popleft() 
                
                current_level_sum += node.val 
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_level = current_level
                
            current_level += 1
            
        return max_level