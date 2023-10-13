"""Longest Subarray of 1's After Deleting One Element
Medium
Topics
Companies
Hint
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1."""

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #print("*"*66)
        left=0
        right=0
        zeros=0
        lenght=len(nums)
        max_ones=0
        if sum(nums)==lenght:
            return lenght-1

        for right in range(lenght):
            if nums[right]==0:
                zeros+=1
                #print(lenght-sum(nums))
                while zeros>1:
                    if nums[left]==0:
                        zeros-=1
                    left+=1
                    #print(f"left {left}")
            max_ones=max(max_ones,right-left)
            #print(f"left {left}")
            #print(f"right {right}")
            #print(f"zeros {zeros}")
            #print(f"max_ones {max_ones}")
        return max_ones



