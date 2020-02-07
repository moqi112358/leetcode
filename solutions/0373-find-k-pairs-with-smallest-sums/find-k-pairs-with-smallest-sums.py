# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
# Example 1:
#
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]] 
# Explanation: The first 3 pairs are returned from the sequence: 
#              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
# Example 2:
#
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence: 
#              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
# Example 3:
#
#
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
#
#


class Solution:
    # Method 1: heapq
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     h = []
    #     import heapq
    #     if not nums1 or not nums2:
    #         return None
    #     for i in nums1:
    #         for j in nums2:
    #             heapq.heappush(h, (i + j, i , j))
    #     res = []
    #     for i in range(k):
    #         if len(h) > 0:
    #             sum_v, v1, v2 = heapq.heappop(h)
    #             res.append([v1, v2])
    #     return res
    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2:
            return []
        from heapq import heappush, heappop
        visited = set()
        heap = []
        output = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while len(output) < k and heap:

            val = heappop(heap)
            output.append((nums1[val[1]], nums2[val[2]]))

            if val[1] + 1 < len(nums1) and (val[1] + 1, val[2]) not in visited:
                heappush(heap, (nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]))
                visited.add((val[1] + 1, val[2]))

            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heappush(heap, (nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1))
                visited.add((val[1], val[2] + 1))

        return output
