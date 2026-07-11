class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        for i in range(len(flowerbed)):

            left = (i == 0) or (flowerbed[i - 1] == 0)

            right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            if flowerbed[i] == 0 and left and right:

                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return n <= 0
def main():
    sol = Solution()
    flowerbed = [1,0,0,0,0,1]
    n = 2
    result = sol.canPlaceFlowers(flowerbed, n)
    print(result)
if __name__ == "__main__":
    main()