import unittest
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """




class TestSolution(unittest.TestCase):
    def test_isAnagram(self):
        cls = Solution()
        r = cls.isAnagram("anagram", "nagaram")
        self.assertEqual(r, True)
        r = cls.isAnagram("rat", "car")
        self.assertEqual(r, False)


if __name__ == "__main__":
    unittest.main()