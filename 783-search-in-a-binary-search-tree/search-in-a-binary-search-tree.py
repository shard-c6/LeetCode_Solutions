# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if root is None or root.val == val:
        #     return root
        
        # if root.val < val:
        #     return self.searchBST(root.right, val)
        
        # return self.searchBST(root.left, val)

        current_node = root
        while current_node is not None:
            if current_node.val == val:
                return current_node
            elif val <= current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
            
        return None