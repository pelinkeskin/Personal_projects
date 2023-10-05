"""
605. Can Place Flowers
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length"""


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zero_sequence_lenghts = []
        count = 0
        for index, number in enumerate(flowerbed):
            if number == 0:
                count += 1
                if index == len(flowerbed)-1 and number == 0:
                    zero_sequence_lenghts += [count]
            else:
                zero_sequence_lenghts += [count]
                count = 0
        try:
            zero_sequence_lenghts.remove(0)
        except:
            zero_sequence_lenghts

        num_place = [(x-1)//2 for x in zero_sequence_lenghts]

        check_full_empty = 0
        for i in flowerbed:
            if i != 0:
                check_full_empty += 1

        if check_full_empty != 0:
            if flowerbed[0] == 0:
                if len(flowerbed) == 1:
                    num_place = [1]
                else:
                    num_place[0] = (zero_sequence_lenghts[0])//2
            if flowerbed[-1] == 0:
                if len(flowerbed) == 1:
                    num_place = [1]
                else:
                    num_place[-1] = (zero_sequence_lenghts[-1])//2
        else:
            num_place = [(x+1)//2 for x in zero_sequence_lenghts]

        if sum(num_place) >= n:
            return True
        else:
            return False
