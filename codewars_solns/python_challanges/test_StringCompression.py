import unittest
from StringCompression import Solution

class test_tringCompression(unittest.TestCase):
    soln=Solution()
    def test(self):
        self.assertEqual(test_tringCompression.soln.compress(["a","a","b","b","c","c","c"]),6)
        self.assertEqual(test_tringCompression.soln.compress(["a"]),1)
        self.assertEqual(test_tringCompression.soln.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]),4)

if __name__=='__main__':
    unittest.main()