class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root=preorder.pop(0)
        root_node=TreeNode(root)
        pos=inorder.index(root)

        if len(inorder)==1:
            return root_node

        left_inoder=inorder[:pos]
        right_inorder=inorder[pos+1:]

        root_node.left=self.buildTree(preorder[:pos],left_inoder)
        root_node.right=self.buildTree(preorder[pos:],right_inorder)
        return root_node







