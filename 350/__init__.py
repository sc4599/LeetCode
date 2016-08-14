__author__ = 'songchao'
import unittest



class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r = []
        i = 0
        max_list = nums1 if len(nums1) > len(nums2) else nums2
        min_list = nums2 if len(nums1) > len(nums2) else nums1
        min_list_len = len(min_list)
        while i < min_list_len:
            if min_list[i] in max_list:
                r.append(min_list[i])
                max_list.remove(min_list[i])
                min_list.remove(min_list[i])
                min_list_len = len(min_list)
            else:
                i += 1
        return r


class TestSolution(unittest.TestCase):
    def test_intersect(self):
        cls = Solution()
        r = cls.intersect([1, 2, 2, 1], [2, 2])
        self.assertEqual(r, [2, 2])
        r1 = cls.intersect([1, 2, 3, 4, 5, 6], [4, 5])
        self.assertEqual(r1, [4, 5])
        r2 = cls.intersect([1, 1], [1])
        self.assertEqual(r2, [1])
        r2 = cls.intersect([3, 2, 1], [1, 1])
        self.assertEqual(r2, [1])


if __name__ == "__main__":
    unittest.main()
    # print ['1', '', None]
