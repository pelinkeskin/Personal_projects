"""1768. Merge Strings Alternately
Easy
Topics
Companies
Hint
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word=""
        for (char1, char2) in zip(word1, word2):
            new_word=new_word+char1+char2
        
        difference=len(word1)-len(word2)
        add=""
        if len(word1)>len(word2):
            add=word1[-difference:]
            print(add)
        elif len(word1)<len(word2):
            add=word2[difference:]
            print(add)
        return new_word+add
    
print(Solution().mergeAlternately("abc","pqr"))
print("*"*40)
print(Solution().mergeAlternately("ab","pqrs"))
print("*"*40)
print(Solution().mergeAlternately("abcd","pq"))
print("*"*40)
print(Solution().mergeAlternately("cdf","a"))