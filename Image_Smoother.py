class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        directions = [
            (-1, 0), 
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (0, 0)
        ]

        for i in range(len(img)):
            for j in range(len(img[0])):
                sum = 0
                dem = 0
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < len(img) and 0 <= nj < len(img[0]):
                        sum += img[ni][nj]
                        dem += 1
                img[i][j] = sum // dem
        return img
def main():
    sol = Solution()
    img = [[100,200,100],[200,50,200],[100,200,100]]
    result = sol.imageSmoother(img)
    print(result)
if __name__ == "__main__":
    main()


