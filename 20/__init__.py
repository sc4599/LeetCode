# coding= utf-8
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        题意：输入一个只包含括号的字符串，判断括号是否匹配
        模拟堆栈，读到左括号压栈，读到右括号判断栈顶括号是否匹配
        """

        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch == ")" and stack[-1] == "(" or ch == "]" and stack[-1] == "[" or ch == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return not stack

import unittest


class TestSolution(unittest.TestCase):
    def test_isValid(self):
        cls = Solution()
        r = cls.isValid("[")
        self.assertEqual(r, False)
        r = cls.isValid("]")
        self.assertEqual(r, False)
        r = cls.isValid("([)]")
        self.assertEqual(r, False)
        r = cls.isValid("(])")
        self.assertEqual(r, False)




if __name__ == "__main__":
    unittest.main()
