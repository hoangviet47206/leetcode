class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        n = len(s)

        for i in range(n):
            if s[i] != " " and (i == n - 1 or s[i + 1] == " "):
                l += 1

        return l
def main():
    sol = Solution()
    s = "Hello, my name is John"
    result = sol.countSegments(s)
    print(result)

if __name__ == "__main__":
    main()