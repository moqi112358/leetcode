# Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
#
# Notice that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#  
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
#  
# Constraints:
#
#
# 	0 <= rowIndex <= 33
#
#


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        index = 1
        queue = [1]
        while index  <= rowIndex:
            tmp = [1]
            for i in range(1, len(queue)):
                tmp.append(queue[i-1] + queue[i])
            tmp.append(1)
            queue = tmp
            index += 1
        return queue
                
            
