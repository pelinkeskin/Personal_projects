import unittest
from SingleNumber import Solution

class test_singleNumber(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.singleNumber([2,2,1]),1)
        self.assertEqual(soln.singleNumber([4,1,2,1,2]),4)
        self.assertEqual(soln.singleNumber([1]),1)
        self.assertEqual(soln.singleNumber([1,0,1]),0)



if __name__=='__main__':
    unittest.main()

