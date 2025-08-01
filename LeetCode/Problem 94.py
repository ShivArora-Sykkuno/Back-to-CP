class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
        inOrder(root)
        return res
    


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []  

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []  
        self.inorder(root)
        return self.res



"""