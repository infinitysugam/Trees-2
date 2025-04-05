# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,0)
    

    def helper(self,root,result):

        if root == None:
            return 0

        if root.left == None and root.right==None:
            return result * 10 + root.val
        
        return self.helper(root.left, result*10 + root.val) + self.helper(root.right, result*10 + root.val)