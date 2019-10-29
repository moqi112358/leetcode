# A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.
#
# What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.
#
#
# Examples:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]
# Explanation:
# The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# The third fraction is 2/5.
#
# Input: A = [1, 7], K = 1
# Output: [1, 7]
#
#
# Note:
#
#
# 	A will have length between 2 and 2000.
# 	Each A[i] will be between 1 and 30000.
# 	K will be between 1 and A.length * (A.length - 1) / 2.
#


class Solution:
    """
    @param A: a list of integers
    @param K: a integer
    @return: return two integers
    """
    def kthSmallestPrimeFraction(self, A, K):
        # write your code here
        l, r = 0, 1.0
        p, q, n, cnt = 0, 1, len(A), 0
        while True:
            cnt, j, p = 0, 0, 0
            mid = (l+r)/2
            for i in range(n):
                while j < n and A[i] / A[j] > mid:
                    j += 1
                cnt += n-j
                if j<n and p / q < A[i] / A[j]:
                    p, q = A[i], A[j]
            
            if cnt == K:
                return [p, q]
            elif cnt < K:
                l = mid
            else:
                r = mid
