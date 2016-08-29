class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        es = [x for x in string.uppercase]
        r = 0
        l = range(len(s))
        l.reverse()
        for i, w in zip(l, s):
            r += 26 ** i * (es.index(w)+1)
        return r


if __name__ == "__main__":
    cls = Solution()
    s = 'AAAB'
    print cls.titleToNumber(s)
    l = ['0', '1', '2']
    # print range(0, 6)

    s = 'ABCD'
    print cls.titleToNumber(s)
