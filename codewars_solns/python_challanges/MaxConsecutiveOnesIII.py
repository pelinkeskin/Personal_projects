"""Max Consecutive Ones III
Medium
Topics
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length"""
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        count_zero=0
        max_seq=0
        for right in range(len(nums)):
            if nums[right]==0:
                count_zero+=1
                while count_zero>k:
                    if nums[left]==0:
                        count_zero-=1
                    left+=1
            max_seq=max(max_seq,right-left+1)
        return max_seq






  





                    


            