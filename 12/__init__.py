# -*- coding: utf-8 -*-
import time
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # roman_dict_str = {
        #     "I": 1, "IV": 4, "V": 5, "IX": 9,
        #     "X": 10, "XL": 40, "L": 50, "XC": 90,
        #     "C": 100, "CD": 400, "D": 500, "CM": 900,
        #     "M": 1000
        # }

        list_ch = list(str(num))
        list_ch.reverse()
        r = ""
        for i in reversed(range(len(list_ch))):
            current_num = int(list_ch[i])
            if i == 3:  # 千位
                r += current_num * "M"
            if i == 2:  # 百位
                if current_num == 0:
                    continue
                if current_num % 9 == 0:
                    r += "CM"
                    current_num -= 9
                elif current_num >= 5:
                    r += "D"
                    current_num -= 5
                elif current_num % 4 == 0:
                    r += "CD"
                    current_num -= 4
                for e in range(current_num):
                    r += "C"
            if i == 1:  # 十位
                if current_num == 0:
                    continue
                if current_num % 9 == 0:
                    r += "XC"
                    current_num -= 9
                elif current_num >= 5:
                    r += "L"
                    current_num -= 5
                elif current_num % 4 == 0:
                    r += "XL"
                    current_num -= 4
                for e in range(int(current_num)):
                    r += "X"
            if i == 0:  # 个位
                if current_num == 0:
                    continue
                if current_num % 9 == 0:
                    r += "IX"
                    current_num -= 9
                elif current_num >= 5:
                    r += "V"
                    current_num -= 5
                    print current_num
                elif current_num % 4 == 0:
                    r += "IV"
                    current_num -= 4

                for e in range(int(current_num)):
                    r += "I"
        return r

    def intToRoman2(self, num):
        dict_str = [{0: 'V', 1: 'VI', 2: 'VII', 3: 'VIII', 4: 'IX', -2: 'III', -4: 'I', -3: 'II', -1: 'IV'},
                    {0: 'L', 1: 'LX', 2: 'LXX', 3: 'LXXX', 4: 'XC', -2: 'XXX', -4: 'X', -3: 'XX', -1: 'XL'},
                    {0: 'D', 1: 'DC', 2: 'DCC', 3: 'DCCC', 4: 'CM', -2: 'CCC', -4: 'C', -3: 'CC', -1: 'CD'},
                    {-4: 'M', -3: 'MM', -2: 'MMM'}]
        b = list(str(num))
        b.reverse()
        r = ''
        for i in reversed(range(len(b))):
            n = int(b[i]) - 5
            if n != -5:
                r += dict_str[i][n]

        return r
        pass

    def intToRoman3(self, num):
        aArray = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        rArray = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        r = ""
        for i in range(len(aArray)):
            while num >= aArray[i]:
                r += rArray[i]
                num -= aArray[i]
        return r


import unittest


class TestSolution(unittest.TestCase):
    def test_intToRoman(self):
        cls = Solution()
        r = cls.intToRoman(2016)
        self.assertEqual(r, "MMXVI")
        r = cls.intToRoman(3999)
        self.assertEqual(r, "MMMCMXCIX")
        r = cls.intToRoman(494)
        self.assertEqual(r, "CDXCIV")
        r = cls.intToRoman(621)
        self.assertEqual(r, "DCXXI")
        r = cls.intToRoman(10)
        self.assertEqual(r, "X")

    def test_intToRoman2(self):
        cls = Solution()
        r = cls.intToRoman2(2016)
        self.assertEqual(r, "MMXVI")
        r = cls.intToRoman2(3999)
        self.assertEqual(r, "MMMCMXCIX")
        r = cls.intToRoman2(494)
        self.assertEqual(r, "CDXCIV")
        r = cls.intToRoman2(621)
        self.assertEqual(r, "DCXXI")
        r = cls.intToRoman2(10)
        self.assertEqual(r, "X")




class TestSolution3(unittest.TestCase):
    def test_intToRoman3(self):
        cls = Solution()
        start = time.time()
        r = cls.intToRoman3(2016)
        self.assertEqual(r, "MMXVI")
        r = cls.intToRoman3(3999)
        self.assertEqual(r, "MMMCMXCIX")
        r = cls.intToRoman3(494)
        self.assertEqual(r, "CDXCIV")
        r = cls.intToRoman3(621)
        self.assertEqual(r, "DCXXI")
        r = cls.intToRoman3(10)
        self.assertEqual(r, "X")
        end = time.time()
        print start
        print end
        print ("Ran tests in %ss"%(str(round(start-end, 3))))

if __name__ == "__main__":
    unittest.main()



    pass
