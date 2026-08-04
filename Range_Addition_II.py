class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        if not ops:
            return m * n

        minl = m
        minr = n
        for a, b in ops:
            minl = min(minl, a)
            minr = min(minr, b)
        return (minl * minr)

def main():
    sol = Solution()
    m = 3
    n = 3
    ops = [[2,2],[3,3]]
    result = sol.maxCount(m, n, ops)
    print(result)
if __name__ == "__main__":
    main()