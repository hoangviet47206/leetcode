class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        check = image[sr - 1][sc - 1]
        for i in range(sr - 1, len(image)):
            for j in range(sc - 1, len(image[0])):
                if check == image[i][j] :
                    image[i][j] = color
                else:
                    break

        return image
def main():
    sol = Solution()
    image = [[0, 0, 0], [0, 0, 1]]
    sr = 0
    sc = 0
    color = 2
    result = sol.floodFill(image, sr, sc, color)
    print(result)
if __name__ == "__main__":
    main()   
