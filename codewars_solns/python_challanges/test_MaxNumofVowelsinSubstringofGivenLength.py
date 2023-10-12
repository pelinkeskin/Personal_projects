import unittest
from MaxNumofVowelsinSubstringofGivenLength import Solution

class test_MaxNumofVowelsinSubstringofGivenLength(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.maxVowels(s = "abciiidef", k = 3),3)
        self.assertEqual(soln.maxVowels(s = "aeiou", k = 2),2)
        self.assertEqual(soln.maxVowels(s = "leetcode", k = 3),2)
        self.assertEqual(soln.maxVowels(s = "weallloveyou", k = 7),4)

if __name__=='__main__':
    unittest.main()