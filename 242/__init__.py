import unittest
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        first_list= [i for i in s]
        second_list = [i for i in t]
        for i in first_list:
            if i in second_list:
                second_list.remove(i)
            else:
                return False
        return True



class TestSolution(unittest.TestCase):
    def test_isAnagram(self):
        cls = Solution()
        r = cls.isAnagram("anagram", "nagaram")
        self.assertEqual(r, True)
        r = cls.isAnagram("rat", "car")
        self.assertEqual(r, False)


if __name__ == "__main__":
    unittest.main()