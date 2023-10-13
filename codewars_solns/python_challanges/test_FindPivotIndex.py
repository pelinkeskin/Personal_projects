import unittest
from FindPivotIndex import Solution

class test_FindPivotIndex(unittest.TestCase):
    def test(self):
        soln = Solution()
        self.assertEqual(soln.pivotIndex([1,7,3,6,5,6]),3 )
        self.assertEqual(soln.pivotIndex([1,2,3]),-1)
        self.assertEqual(soln.pivotIndex([2,1,-1]),0 )
        self.assertEqual(soln.pivotIndex([-1,-1,-1,-1,-1,0]),2 )

if __name__ == '__main__':
    unittest.main()

