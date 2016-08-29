class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        max_nums = nums1 if len(nums1) > len(nums2) else nums2
        min_nums = nums1 if len(nums1) < len(nums2) else nums2
        r_nums = set()
        for i in min_nums:
            if i in max_nums:
                r_nums.add(i)
        return list(r_nums)

    def intersection_b(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
