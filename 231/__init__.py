# coding=utf-8
__author__ = 'songchao'

   # 将2的幂次方写成二进制形式后，很容易就会发现有一个特点：二进制中只有一个1，并且1后面跟了n个0；
   #  因此问题可以转化为判断1后面是否跟了n个0就可以了。
   #      如果将这个数减去1后会发现，仅有的那个1会变为0，而原来的那n个0会变为1；
   # 因此将原来的数与去减去1后的数字进行与运算后会发现为零。
   #     最快速的方法：
   #
   #    (number & number - 1) == 0
   #
   #    原因：因为2的N次方换算是二进制为10……0这样的形式(0除外)。与上自己-1的位数，这们得到结果为0。
   # 例如。8的二进制为1000；8-1=7，7的二进制为111。两者相与的结果为0。计算如下：
   #       1000
   #     & 0111
   #      -------
   #       0000
   #
   #   使用递归来实现的代码如下：


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n&(n-1) == 0


import unittest


class TestSolution(unittest.TestCase):
    def test_isPowerOfTwo(self):
        cls = Solution()
        r = cls.isPowerOfTwo(1)
        self.assertEqual(r, True)
        self.assertEqual(cls.isPowerOfTwo(2), True)
        self.assertEqual(cls.isPowerOfTwo(6), False)
        self.assertEqual(cls.isPowerOfTwo(8), True)
