# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]
        count = [0]

        def dfs(root):
            if not root:
                return None

            left = dfs(root.left)
            count[0] += 1

            if count[0] == k:
                ans[0] = root.val
                return root.val

            right = dfs(root.right)

            return root.val
        
        dfs(root)

        return ans[0]