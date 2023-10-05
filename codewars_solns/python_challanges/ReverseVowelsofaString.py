"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters."""

from typing import List

class Solution:
    def get_vowels_reverse(self, s: str) -> List[str]:
        vowels=[]
        for i in s:
            if i in ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']:
                vowels.append(i)
        vowels.reverse()
        return vowels


    def reverseVowels(self, s: str) -> str:
        reverse_vowel_list= self.get_vowels_reverse(s)
        count=0
        new_word=""
        for i in s:
            if i in ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']:
                new_word+=reverse_vowel_list[count]
                count+=1
            else:
                new_word+=i
        return new_word