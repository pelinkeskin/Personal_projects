import unittest

from ProductofArrayExceptSelf import Solution

class test_ProductofArrayExceptSelf(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.productExceptSelf([1,2,3,4]),[24,12,8,6])
        self.assertEqual(soln.productExceptSelf([-1,1,0,-3,3]),[0,0,9,0,0])

if __name__=='__main__':
    unittest.main()