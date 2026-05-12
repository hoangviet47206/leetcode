class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(0, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n = n - 1
        return (n == 0)
def main():
    sol = Solution()
    flowerbed = [1,0,0,0,0,1]
    n = 2
    result = sol.canPlaceFlowers(flowerbed, n)
    print(result)
if __name__ == "__main__":
    main()