class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traversal(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            return (traversal(node1.left, node2.left) and 
                    traversal(node1.right, node2.right))
        
        return traversal(p, q)