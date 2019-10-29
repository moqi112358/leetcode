# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
#
#  
#
# Example 1:
#
#
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
#  
#
# Note:
#
#
# 	A.length <= 30000
# 	0 <= S <= A.length
# 	A[i] is either 0 or 1.
#


class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        tmp = []
        res = 0
        for i in range(len(A)):
            if A[i] == 1:
                tmp.append(i)
        i, j = 0, S-1
        if len(tmp) < S:
            return 0
        if S == 0:
            i = 0
            if len(tmp) == 0:
                return int(len(A) * (len(A) + 1) / 2)
            while i < len(tmp) - 1:
                x = tmp[i+1] - tmp[i] - 1
                res += (x*(x+1)/2)
                i += 1
            x = len(A) - tmp[i] - 1
            res += (x*(x+1)/2)
            if tmp[0] != 0:
                x = tmp[0]
                res += (x*(x+1)/2)
            return int(res)
                
        while j < len(tmp):
            if i == 0 and j != len(tmp) - 1:
                res += ((tmp[j+1] - tmp[j]) * (tmp[i] + 1))
                i += 1
                j += 1
                continue
            if i == 0 and j == len(tmp) - 1:
                res += ((len(A) - tmp[j]) * (tmp[i] + 1))
                i += 1
                j += 1
                continue
            if i != 0 and j == len(tmp) - 1:
                res += ((len(A) - tmp[j]) * (tmp[i] - tmp[i-1]))
                i += 1
                j += 1
                continue
            if i != 0 and j != len(tmp) - 1:
                res += ((tmp[j+1]- tmp[j]) * (tmp[i] - tmp[i-1]))
                i += 1
                j += 1
                continue
        return res
            
            
            
            
                
            
