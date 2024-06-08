# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        '''
        Order: inorder, preorder, postorder
        Goal: traverse a tree and convert to either in/pre/post order

        Preorder: keep going left until you cannot and then pop back up
        '''
        preorder = []

        def dfs(root):
            if not root:
                preorder.append("N")
                return

            preorder.append(str(root.val))

            left = dfs(root.left)
            right = dfs(root.right)

            return root.val
        
        dfs(root)
        print(preorder)
        return ",".join(preorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.i = 0

        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))