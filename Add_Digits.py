class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if (num < 10) : return num
        while(num >= 10 ):
            re = 0
            while(num > 0):
                re = re + num % 10
                num = num // 10 
            
            num = re
        
        return num
def main():
    sol = Solution()
    num = 38
    result = sol.addDigits(num)
    print(result)

if __name__ == "__main__":
    main()