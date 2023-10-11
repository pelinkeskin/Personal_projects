import unittest
from MaximumAverageSubarrayI import Solution

class test_MaximumAverageSubarrayI(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4),12.75000)
        self.assertEqual(soln.findMaxAverage(nums = [5], k = 1),5.00000)
        self.assertEqual(soln.findMaxAverage(nums = [0,1,1,3,3], k = 4),2.00000)


if __name__=='__main__':
    unittest.main()