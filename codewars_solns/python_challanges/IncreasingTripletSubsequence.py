"""334. Increasing Triplet Subsequence
Medium
Topics
Companies
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
from typing import List

class Solution: 
    def increasingTriplet(self, nums: List[int]) -> bool:
        sort_list=[]
        for i,n in enumerate(nums):
            if i==0 or i == len(nums)-1:
                sort_list+=[n]
            if n!=nums[i-1]:
                sort_list+=[n]
        
        if len(set(sort_list))<3:
            return False
                
        #print("*"*66)
        #print(sort_list)
        for i,n in enumerate(sort_list):
            if i !=0:
                left_side=sort_list[:i]
                
                right_side=sort_list[i:]
                
                if min(left_side)<n and max(right_side)>n:
                    return True
            elif i ==-1:
                return False


        



            
#print(Solution().increasingTriplet([20,100,10,12,5,13]))
#print(Solution().increasingTriplet([5,4,3,2,1]))
#print(Solution().increasingTriplet([1,2,3,4,5]))
#print(Solution().increasingTriplet([2,1,5,0,4,6]))