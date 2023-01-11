import unittest
from CodewarsStyleRankingSystem import User

class TestCodewarsStyleRankingSystem(unittest.TestCase):
    def test(self):
        user = User()
        self.assertEqual(user.rank, -8)
        self.assertEqual(user.progress, 0)
        user.inc_progress(-7)
        self.assertEqual(user.progress, 10)
        user.inc_progress(-5)
        self.assertEqual(user.progress, 0)
        self.assertEqual(user.rank, -7)
        user.inc_progress(-3)
        self.assertEqual(user.progress, 60)
        self.assertEqual(user.rank, -6)