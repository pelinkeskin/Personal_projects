import unittest
from UniqueNumberofOccurrences import Solution

class test_UniqueNumberofOccurrences(unittest.TestCase):
    def test(self):
        soln=Solution()

        self.assertTrue(soln.uniqueOccurrences([1,2,2,1,1,3]))
        self.assertFalse(soln.uniqueOccurrences([1,2]))
        self.assertTrue(soln.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))

if __name__ == '__main__':
    unittest.main()