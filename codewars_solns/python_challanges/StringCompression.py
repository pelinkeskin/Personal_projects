"""443. String Compression
Medium
Topics
Companies
Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space."""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        count=0
        compressed=""
        for i,n in enumerate(chars):
            if i==0:
                compressed=n
                count+=1
            else:
                if n==chars[i-1]:
                    count+=1
                    if i==len(chars)-1:
                        if count != 1:
                            compressed+=str(count)
                else:
                    if count != 1:
                        compressed+=str(count)
                    count=1
                    compressed+=n
        for i,x in enumerate(compressed):
                chars[i]=x
        chars=chars[:len(compressed)]
        
        return len(chars)


