import unittest
from ReverseWordsinaString import Solution

class test_ReverseWordsinaString(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.reverseWords("the sky is blue"),"blue is sky the")
        #Explanation: Your reversed string should not contain leading or trailing spaces.
        self.assertEqual(soln.reverseWords("  hello world  "),"world hello")
        #Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
        self.assertEqual(soln.reverseWords("a good   example"),"example good a")

if __name__== '__main__':
    unittest.main()