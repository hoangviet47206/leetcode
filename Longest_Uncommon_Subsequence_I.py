class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        tmp = max(self.diffchar(a, b), self.diffchar(b, a))
        
        return -1 if tmp == 0 else tmp
    def diffchar(self, a, b):
        dem = 0
        for i in a:
            for j in b:
                if a != b:
                    dem = dem + 1
                    break
        
        return dem

def main():
    sol = Solution()
    result = sol.findLUSlength(a="ab", b="def")
    print(result)
if __name__ == "__main__":
    main()