import unittest
from MaxConsecutiveOnesIII import Solution

class test_MaxConsecutiveOnesIII(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2),6)
        self.assertEqual(soln.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3),10)
        self.assertEqual(soln.longestOnes(nums = [0,0,1,1,1,0,0], k = 0),3)
        self.assertEqual(soln.longestOnes(nums = [0,0,0,1], k = 4),4)
        self.assertEqual(soln.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1], k = 0),4)
        self.assertEqual(soln.longestOnes(nums = [1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], k = 8),25)

if __name__ =='__main__':
    unittest.main()