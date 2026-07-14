class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        diff = (sumB - sumA) // 2

        bobSet = set(bobSizes)

        for x in aliceSizes:
            if x + diff in bobSet:
                return [x, x + diff]
def main():
    aliceSizes = [2]
    bobSizes = [1, 3]

    sol = Solution()
    result = sol.fairCandySwap(aliceSizes, bobSizes)

    print("Kẹo của Alice:", aliceSizes)
    print("Kẹo của Bob:", bobSizes)
    print("Kết quả trao đổi:", result)


if __name__ == "__main__":
    main()

