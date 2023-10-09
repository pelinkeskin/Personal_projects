"""1318. Minimum Flips to Make a OR b Equal to c
Medium
Topics
Companies
Hint
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Example 1:

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 
Constraints:
1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a==b==c:
            return 0
        
        bina=bin(a)[2:]
        binb=bin(b)[2:]
        binc=bin(c)[2:]
        lenght=max(len(bina),len(binb),len(binc))
        if len(bina)<lenght:
            dif=lenght-len(bina)
            bina=dif*'0'+bina
        if len(binb)<lenght:
            dif=lenght-len(binb)
            binb=dif*'0'+binb
        if len(binc)<lenght:
            dif=lenght-len(binc)
            binc=dif*'0'+binc

        count=0
        for ca, cb, cc in zip(bina,binb,binc):

            if not (int(ca) or int(cb)) ==int(cc):
                if int(cc)==0:
                    if int(ca)==int(cb)==1:
                        count+=2
                    else:
                        count+=1
                else:
                    count+=1

        return count


