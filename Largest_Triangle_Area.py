class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        result = -1
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    Sare = abs(points[i][0] * (points[j][1] -  points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0] * (points[i][1] - points[j][1]))
                    result = max(result, Sare / 2)
        return result
def main():
    sol = Solution()
    result = sol.largestTriangleArea(points = [[0,0],[0,1],[1,0],[0,2],[2,0]])
    print(result)
if __name__ == "__main__":
    main()