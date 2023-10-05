import unittest
from KidsWiththeGreatestNumberofCandies import Solution

class test_KidsWithGreatestNumberofCandies(unittest.TestCase):
    def test(self):
        soln = Solution()
        self.assertEqual(soln.kidsWithCandies([2,3,5,1,3],3),[True,True,True,False,True] )
        self.assertEqual(soln.kidsWithCandies([4,2,1,1,2],1),[True,False,False,False,False])
        self.assertEqual(soln.kidsWithCandies([12,1,12],10),[True,False,True] )

if __name__ == '__main__':
    unittest.main()