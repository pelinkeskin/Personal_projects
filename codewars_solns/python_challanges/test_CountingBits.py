import unittest
from CountingBits import Solution

class test_CountingBits(unittest.TestCase):
    def test(self):
        soln = Solution()
        self.assertEqual(soln.countBits(2),[0,1,1] )
        self.assertEqual(soln.countBits(5),[0,1,1,2,1,2] )


if __name__ == '__main__':
    unittest.main()