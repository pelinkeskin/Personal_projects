"""1456. Maximum Number of Vowels in a Substring of Given Length
Medium
Topics
Companies
Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length"""

class Solution:
    def vowel_count(self,mystr):
        vowels=['a', 'e', 'i', 'o','u']
        count=0
        for i in mystr:
            if i in vowels:
                count+=1
        return count

    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a', 'e', 'i', 'o','u']
        i=1
        substring=s[:k]
        window_max_vow=self.vowel_count(substring)
        substr_vow_c=self.vowel_count(substring)
        while i<len(s)-k+1:
            if substring[0] in vowels:
                substr_vow_c-=1
            substring=substring[1:]+str(s[i+k-1])
            if substring[-1] in vowels:
                substr_vow_c+=1
            if substr_vow_c==k:
                return k
            elif substr_vow_c>window_max_vow:
                window_max_vow=substr_vow_c
            i+=1
        return window_max_vow