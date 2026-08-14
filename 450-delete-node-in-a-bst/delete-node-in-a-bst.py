# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        # Found the node!
        else:
            # Case 1 & 2: 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
                
            # Case 3: 2 children
            # Find the in-order successor (smallest in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
                
            # Copy the successor's value to the current node
            root.val = curr.val
            
            # Delete the original successor node from the right subtree
            root.right = self.deleteNode(root.right, root.val)
            
        return root