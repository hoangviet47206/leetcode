class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        check = sorted(heights)
        result = 0

        for i in range(0, len(heights)):
            if (heights[i] != check[i]):
                result += 1

        return result

def main():
    sol = Solution()
    heights = [1,1,4,2,1,3]

    result =  sol.heightChecker(heights)
    print(result)

if __name__ == "__main__":
    main()