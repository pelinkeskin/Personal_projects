"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's 
in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?"""
from typing import List

class Solution:
    
    def countBits(self, n: int) -> List[int]:
        print("*"*66)
        ans=[]
        for i in range(n+1):
            print(i)
            binary_i=bin(i)
            binary_char_list=[i for i in binary_i]
            print(binary_char_list)
            if i ==0:
                ans.append(0)
            elif i==1:
                ans.append(1)
            else:
                ans.append(binary_char_list.count('1'))
        return ans
                    
#without bin function
class Solution2:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            c=i
            bits=[]
            while i != 0:
                bits+= [i%2]
                i=i//2

            if c == 0:
                ans +=[0]
            elif c == 1:
                ans +=[1]
            else:
                ans+=[bits.count(1)]
        return ans

