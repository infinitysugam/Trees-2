# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(postorder)==0:
            return None
        
        root = TreeNode(postorder[-1])



        index = -1
        for i in range(0,len(inorder)):
            if root.val == inorder[i]:
                index = i
                break
        
        inorder_l = inorder[:index]
        inorder_r = inorder[index+1:len(inorder)]

        postorder_l = postorder[:len(inorder_l)]
        postorder_r = postorder[len(inorder_l):-1]


        root.left = self.buildTree(inorder_l,postorder_l)
        root.right = self.buildTree(inorder_r,postorder_r)
        return root
