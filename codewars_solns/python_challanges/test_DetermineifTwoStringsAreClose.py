import unittest
from DetermineifTwoStringsAreClose import Solution

class test_DetermineifTwoStringsAreClose(unittest.TestCase):
    def test(self):
        soln=Solution()
        message = "Test failed."
        self.assertTrue(soln.closeStrings(word1 = "abc", word2 = "bca"),message)
        self.assertFalse(soln.closeStrings(word1 = "a", word2 = "aa"),message)
        self.assertTrue(soln.closeStrings(word1 = "cabbba", word2 = "abbccc"),message)
        self.assertFalse(soln.closeStrings(word1 = "uau", word2 = "ssx"),message)

if __name__ == '__main__':
    unittest.main()