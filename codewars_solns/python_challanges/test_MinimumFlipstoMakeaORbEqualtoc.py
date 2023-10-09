import unittest
from MinimumFlipstoMakeaORbEqualtoc import Solution

class test_MinimumFlipstoMakeaORbEqualtoc(unittest.TestCase):
    def test(self):
        soln=Solution()
        self.assertEqual(soln.minFlips(a = 2, b = 6, c = 5),3)
        self.assertEqual(soln.minFlips(a = 4, b = 2, c = 7),1)
        self.assertEqual(soln.minFlips(a = 1, b = 2, c = 3),0)

if __name__ =='__main__':
    unittest.main()