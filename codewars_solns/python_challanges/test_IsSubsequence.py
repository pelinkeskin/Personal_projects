import unittest
from IsSubsequence import Solution

class test_IsSubsequence(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertTrue(soln.isSubsequence(s = "abc", t = "ahbgdc"))
        self.assertFalse(soln.isSubsequence(s = "axc", t = "ahbgdc"))
        self.assertFalse(soln.isSubsequence(s = "acb", t = "ahbgdc"))
        self.assertTrue(soln.isSubsequence(s = "ab", t = "baab"))

if __name__=='__main__':
    unittest.main()