# Given a square array of integers A, we want the minimum sum of a falling path through A.
#
# A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.
#
#  
#
# Example 1:
#
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 12
# Explanation: 
# The possible falling paths are:
#
#
#
# 	[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# 	[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# 	[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
#
#
# The falling path with the smallest sum is [1,4,7], so the answer is 12.
#
#  
# Constraints:
#
#
# 	1 <= A.length == A[0].length <= 100
# 	-100 <= A[i][j] <= 100
#
#


class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        dp = [[float('inf')] * n for i in range(m)]
        for i in range(n):
            dp[m-1][i] = A[m-1][i]
        for i in range(m-2,-1,-1):
            for j in range(n):
                tmp1 = tmp2 = tmp3 = float('inf')
                if n - 1 >= j - 1 >= 0:
                    tmp1 = dp[i+1][j-1]
                if n - 1 >= j >= 0:
                    tmp2 = dp[i+1][j]
                if n - 1 >= j + 1 >= 0:
                    tmp3 = dp[i+1][j+1]
                dp[i][j] = A[i][j] + min(tmp1,tmp2,tmp3)
        return min(dp[0])
        '''
        res = float('inf')
        m, n = len(A), len(A[0])
        for i in range(n):
            res = min(res,self.dfs(A,0,i,m,n))
        return res
    
    def dfs(self, A, i, j, m, n):
        tmp1 = tmp2 = tmp3 = float('inf')
        if i == m - 1:
            return A[i][j]
        else:
            if n - 1 >= j - 1 >= 0:
                tmp1 = self.dfs(A,i+1,j-1,m,n)
            if n - 1 >= j >= 0:
                tmp2 = self.dfs(A,i+1,j,m,n)
            if n - 1 >= j + 1 >= 0:
                tmp3 = self.dfs(A,i+1,j+1,m,n)
            return A[i][j] + min(tmp1,tmp2,tmp3)
        '''
                                       
            
