class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        first_position = -1
        last_position = -1
        if target in nums:
            first_position = nums.index(target)
            n = nums[first_position]
            while n== nums[first_position+1]:
                count +=1

            nums.remove(target)
            count += 1
        if count:
            last_position = first_position + count

        return [first_position, last_position]


import unittest


class TestSolution(unittest.TestCase):
    def test_searchRange(self):
        cls = Solution()
        r = cls.searchRange([1], 0)
        self.assertEquals(r, [-1, -1])
        r = cls.searchRange([5, 7, 7, 8, 8, 10], 8)
        self.assertEquals(r, [3, 4])


if __name__ == "__main__":
    unittest.main()