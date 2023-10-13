import unittest
from LongestSubarrayof1sAfterDeletingOneElement import Solution

class test_LongestSubarrayof1sAfterDeletingOneElement(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.longestSubarray([1,1,0,1]),3)
        self.assertEqual(soln.longestSubarray([0,1,1,1,0,1,1,0,1]),5)
        self.assertEqual(soln.longestSubarray([1,1,1]),2)

if __name__ == '__main__':
    unittest.main()