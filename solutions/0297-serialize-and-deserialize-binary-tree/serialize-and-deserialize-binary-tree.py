# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
#
#  
# Example 1:
#
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,2]
# Output: [1,2]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 104].
# 	-1000 <= Node.val <= 1000
#
#


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
        res = []
        if not root:
            return ''
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node != '#':
                res.append(str(node.val))
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append('#')
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append('#')
            else:
                res.append('#')
        return ','.join(res)
            
        

    def deserialize(self, raw_data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(raw_data)
        data = raw_data.split(',')
        if len(raw_data) == 0:
            return None
        root_val = data.pop(0)
        queue = [TreeNode(int(root_val))]
        root = queue[0]
        while queue and len(data) > 0:
            node = queue.pop(0)
            l = data.pop(0)
            r = data.pop(0)
            if l == '#':
                node.left = None
            else:
                left_node = TreeNode(int(l))
                node.left = left_node
                queue.append(left_node)
            if r == "#":
                node.right = None
            else:
                right_node = TreeNode(int(r))
                node.right = right_node
                queue.append(right_node)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
