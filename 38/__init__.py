# coding:utf-8
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        result = self.countAndSay(n - 1)+"&"
        count = 1;
        r = ""
        for i in range(len(result)-1):
            if result[i] == result[i + 1]:
                count += 1
            else:
                r += str(count) + result[i]
                count = 1
        return r


import unittest


class TestSolution(unittest.TestCase):
    def test_countAndSay(self):
        cls = Solution()
        r = cls.countAndSay(1)
        self.assertEqual(r, "1")
        r = cls.countAndSay(2)
        self.assertEqual(r, "11")
        r = cls.countAndSay(3)
        self.assertEqual(r, "21")
        r = cls.countAndSay(4)
        self.assertEqual(r, "1211")
        r = cls.countAndSay(5)
        self.assertEqual(r, "111221")
        r = cls.countAndSay(6)
        self.assertEqual(r, "312211")


if __name__ == "__main__":
    unittest.main()
