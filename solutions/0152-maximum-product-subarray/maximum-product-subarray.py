# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_cut = []
        tmp = []
        product_list = []
        for i in range(len(nums)):
            if nums[i] != 0:
                tmp.append(nums[i])
            if nums[i] == 0 or i == len(nums) - 1:
                if len(tmp) != 0:
                    product_list.append(self.calProduct(tmp))
                    nums_cut.append(tmp)
                    tmp = []
        if len(product_list) == 0:
            return 0
        tmp_res1 = max(product_list)
        tmp_res2 = max([abs(i) for i in product_list])
        if tmp_res1 == tmp_res2:
            return tmp_res1
        else:
            return self.calMaxProduct(tmp_res1, nums_cut, product_list, nums)
        
    
    def calProduct(self, nums):
        res = 1
        for i in nums:
            res *= i
        return res
    
    def calMaxProduct(self, m, nums_cut, product_list, nums):
        res = m
        for p in range(len(product_list)):
            if abs(product_list[p]) > m:
                res = max(res, self.helper(nums_cut[p], product_list[p]))
        if 0 in nums:
            return max(0, res)
        else:
            return res
    
    def helper(self, nums, product):
        if len(nums) == 1:
            return product
        p1 = 1
        p2 = 1
        for i in nums:
            if i > 0:
                p1 *= i
            else:
                p1 *= i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > 0:
                p2 *= nums[i]
            else:
                p2 *= nums[i]
                break
        return int(max(product / p1, product / p2))


        
        
                
        
                
        
