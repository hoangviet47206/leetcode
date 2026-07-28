class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """

        result = [0] * 2
        result[0] = 1

        lenW = 0  # len dong
        for i in s :
            lenc = widths[ord(i) - 97]   # vi tri ki tu
            if (lenW + lenc <= 100):
                lenW = lenW + lenc
            else :
                result[0] = result[0] + 1
                lenW = 0
                lenW = lenW + lenc

        result[1] = lenW

        return result
def main():
    sol = Solution()
    widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    s = "bbbcccdddaaa"
    result = sol.numberOfLines(widths, s)
    print(result)
if __name__ == "__main__":
    main()

            
