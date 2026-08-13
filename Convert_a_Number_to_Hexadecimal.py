class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return ""
        num = num if num >= 0 else num + 2**32
        hexa = "0123456789abcdef"
        result = ""
        while (num > 0):
            tmp = num % 16
            result = hexa[tmp] + result
            num = num // 16
        
        return result
def main():
    sol = Solution()
    num = -1
    result = sol.toHex(num)
    print(result)
if __name__ == "__main__":
    main()
            
            