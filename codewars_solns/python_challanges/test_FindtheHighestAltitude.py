import unittest
from FindtheHighestAltitude import Solution

class test_FindtheHighestAltitude(unittest.TestCase):
    def test(self):
        soln = Solution()
        self.assertEqual(soln.largestAltitude([-5,1,5,0,-7]),1)
        self.assertEqual(soln.largestAltitude([-4,-3,-2,-1,4,3,2]),0)

if __name__ == '__main__':
    unittest.main()