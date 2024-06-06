# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Be mindful of splitting
        [5,9,20,null,null,15,7]

        We cannot traverse from 
        9 > 5 > 20 > BOTH 15 AND 7

        The path can either be
        9 > 5 > 20 > 15

        OR

        9 > 5 > 20 > 7

        '''
        ans  = [root.val] 

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            left = max(left, 0)
            right = max(right, 0)

            ans[0] = max(ans[0], root.val + left + right)

            return root.val + max(left, right)
        
        dfs(root)
        
        return ans[0]