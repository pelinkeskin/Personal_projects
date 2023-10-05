import unittest
from ReverseVowelsofaString import Solution

class test_ReverseVowelsofaString(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.reverseVowels("hello"),"holle")
        self.assertEqual(soln.reverseVowels("leetcode"),"leotcede")

if __name__=='__main__':
    unittest.main()