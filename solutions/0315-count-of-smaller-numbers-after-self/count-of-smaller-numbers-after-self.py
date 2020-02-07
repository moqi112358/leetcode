# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
#
# Example:
#
#
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#


class Solution:
    def countSmaller(self, nums):
        res = [0] * len(nums)
        T = BinarySearchTree()
        for i in range(len(nums)-1, -1, -1):
            res[i] = T.insert(nums[i])
        return res

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.left_smaller = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        count = 0
        if self.root is None:
            self.root = TreeNode(val)
            return count
        root = self.root
        while root:
            if val > root.val:
                count += root.count + root.left_smaller
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
            elif val < root.val:
                root.left_smaller += 1
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            elif val == root.val:
                count += root.left_smaller
                root.count += 1
                break
        return count
    
    # def countSmaller(self, nums):
    #     def sort(enum):
    #         half = len(enum) / 2
    #         if half:
    #             left, right = sort(enum[:half]), sort(enum[half:])
    #             for i in range(len(enum))[::-1]:
    #                 if not right or left and left[-1][1] > right[-1][1]:
    #                     smaller[left[-1][0]] += len(right)
    #                     enum[i] = left.pop()
    #                 else:
    #                     enum[i] = right.pop()
    #         return enum
    #     smaller = [0] * len(nums)
    #     sort(list(enumerate(nums)))
    #     return smaller
        
