class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        arr = [0] * 32
        index = 0 
        while (n > 0):
            c = n % 2 
            n = n // 2

            arr[index] = "0" if (c == 0) else "1"
            if (index > 0) and (arr[index] == arr[index - 1]):
                return False
            index = index + 1
            

        return True 

def main():
    sol = Solution()
    result = sol.hasAlternatingBits(7)
    print(result)
if __name__ == "__main__":
    main()

