class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sumA = 0
        lenL = 0
        tmp = 0
        for i in range(0, len(s)):
            if s[i] == 'A': sumA = sumA + 1
            if s[i] == 'L': 
                tmp = tmp + 1
                lenL = max(lenL, tmp)
            else :
                tmp = 0
        return ((sumA < 3) and (lenL < 3))

def main():
    sol = Solution()
    result = sol.checkRecord(s = "AA")
    print(result)
if __name__ == "__main__":
    main()