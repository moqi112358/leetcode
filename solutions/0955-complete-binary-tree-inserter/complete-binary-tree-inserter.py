# -*- coding:utf-8 -*-


# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
#
# Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:
#
#
# 	CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
# 	CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
# 	CBTInserter.get_root() will return the head node of the tree.
#
#
#
#
#
#
#  
#
# Example 1:
#
#
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
#
#
#
# Example 2:
#
#
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]
#
#
#
#  
#
# Note:
#
#
# 	The initial given tree is complete and contains between 1 and 1000 nodes.
# 	CBTInserter.insert is called at most 10000 times per test case.
# 	Every value of a given or inserted node is between 0 and 5000.
#
#
#
#
#
#  
#
#  
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        l = []
        s = [root]
        
        while s:
            tmp = s.pop(0)
            l.append(tmp.val)
            if tmp.left:
                s.append(tmp.left)
            if tmp.right:
                s.append(tmp.right)
        self.head = None
        self.queue = []
        self.parent = []
        for i in l:
            if self.head is None:
                self.head = TreeNode(i)
                self.queue.append(0)
                self.queue.append(1)
                self.parent.append(self.head)
                self.parent.append(self.head)
            else:
                node = self.queue.pop(0)
                par = self.parent.pop(0)
                if node == 0:
                    par.left = TreeNode(i)
                    self.parent.append(par.left)
                    self.parent.append(par.left)
                elif node == 1:
                    par.right = TreeNode(i)
                    self.parent.append(par.right)
                    self.parent.append(par.right)
                self.queue.append(0)
                self.queue.append(1)


    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        if self.head is None:
            self.head = TreeNode(v)
            return None
        else:
            node = self.queue.pop(0)
            par = self.parent.pop(0)
            if node == 0:
                par.left = TreeNode(v)
                self.parent.append(par.left)
                self.parent.append(par.left)
            elif node == 1:
                par.right = TreeNode(v)
                self.parent.append(par.right)
                self.parent.append(par.right)
            self.queue.append(0)
            self.queue.append(1)
            return par.val

        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.head


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
