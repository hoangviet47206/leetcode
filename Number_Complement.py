class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = ""

        while(num > 0):
            c = num % 2
            num = num // 2
            result = "0" + result if c == 1 else "1" + result

        num = 0
        for i in result:
            num = num * 2 + int(i)
        return num
        
def main():
    sol = Solution()
    num = 5
    result = sol.findComplement(num)
    print(result)
if __name__ == "__main__":
    main()        