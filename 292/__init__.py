class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


import unittest


class TestSolution(unittest.TestCase):
    def test_canWinNim(self):
        cls = Solution()
        r = cls.canWinNim(4)
        self.assertEqual(r, False)
        r = cls.canWinNim(3)
        self.assertEqual(r, True)
        r = cls.canWinNim(2)
        self.assertEqual(r, True)
        r = cls.canWinNim(1)
        self.assertEqual(r, True)
        r = cls.canWinNim(5)
        self.assertEqual(r, True)


if __name__ == "__main__":
    unittest.main()
