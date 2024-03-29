# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            temp = stack.pop()
            ret.append(temp.val)
            root = temp.right
        return ret
