import unittest
from MoveZeroes import Solution

class test_MoveZeroes(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.moveZeroes([0,1,0,3,12]),[1,3,12,0,0])
        self.assertEqual(soln.moveZeroes([0]),[0])

if __name__=='__main__':
    unittest.main()
