# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
         4
       /   \
      2     7
     / \   / \
    1   3 6   9

         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    """

    def invertTree(self, root: TreeNode) -> TreeNode:

        if root.right is not None:
            right = self.invertTree(TreeNode(root.right))

        if root.left is not None:
            left = self.invertTree(TreeNode(root.left))

        root.left = right
        root.right = left

        return root

if __name__ == "__main__":
        sln = Solution()
        rt = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))

        res = sln.invertTree(rt)

        print(res)