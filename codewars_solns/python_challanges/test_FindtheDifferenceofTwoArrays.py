import unittest
from FindtheDifferenceofTwoArrays import Solution

class test_FindtheDifferenceofTwoArrays(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]),[[1,3],[4,6]])
        self.assertEqual(soln.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]),[[3],[]])
        self.assertEqual(soln.findDifference(nums1 = [-68,-80,-19,-94,82,21,-43], nums2 = [-63]),[[-94, -19, -80, 82, 21, -43, -68],[-63]])

if __name__ == '__main__':
    unittest.main()