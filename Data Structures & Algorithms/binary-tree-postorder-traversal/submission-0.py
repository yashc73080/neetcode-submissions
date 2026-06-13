# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        solution = []
        self.postorderHelper(root, solution)
        return solution
        
    def postorderHelper(self, root, solution):
        if root is None:
            return

        self.postorderHelper(root.left, solution)
        self.postorderHelper(root.right, solution)
        solution.append(root.val)