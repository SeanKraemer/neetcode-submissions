# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValueNode(self, root: TreeNode) -> TreeNode:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. Traverse the tree to find the target node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # 2. Case 1 & 2: Node with 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # 3. Case 3: Node with 2 children
            minNode = self.minValueNode(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
            
        return root