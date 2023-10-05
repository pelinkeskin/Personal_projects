import unittest
from CanPlaceFlowers import Solution

class test_CanPlaceFlowers(unittest.TestCase):
    def test(self):
        soln=Solution()
        message = "Test failed."
        self.assertTrue(soln.canPlaceFlowers([1,0,0,0,1],1),message)
        self.assertFalse(soln.canPlaceFlowers([1,0,0,0,1],2),message)
        self.assertFalse(soln.canPlaceFlowers([1,0,0,0,0,1],2),message)
        self.assertTrue(soln.canPlaceFlowers([1,0,0,0,0,0,1],2),message)
        self.assertTrue(soln.canPlaceFlowers([1,0,0,0,1,0,0],2),message)
        self.assertTrue(soln.canPlaceFlowers([0],1),message)
        self.assertTrue(soln.canPlaceFlowers([0,0,0],2),message)

if __name__ == '__main__':
    unittest.main()