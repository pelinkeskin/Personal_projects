"""
643. Maximum Average Subarray I
Easy
Topics
Companies
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums)==1:
            return nums[0]
        elif len(nums)==k:
            return sum(nums)/float(k)
        else:
            i=1
            nsum=sum(nums[:k])
            avg_max=nsum/k
            while (i+k) <= len(nums):

                nsum+=nums[i+k-1]-nums[i-1]
                slice_avg=nsum/float(k)
                if slice_avg>avg_max:
                    avg_max=slice_avg
                i+=1
            return avg_max

