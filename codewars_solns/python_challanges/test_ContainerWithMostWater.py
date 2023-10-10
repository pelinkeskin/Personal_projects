import unittest
from ContainerWithMostWater import Solution

class test_ContainerWithMostWater(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.maxArea([1,8,6,2,5,4,8,3,7]),49)
        self.assertEqual(soln.maxArea([1,1]),1)
        self.assertEqual(soln.maxArea([4,3,2,1,4]),16)

if __name__ =='__main__':
    unittest.main()