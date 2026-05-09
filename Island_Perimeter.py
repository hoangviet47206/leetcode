class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        P = 0
        directions = [
            (-1, 0), 
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    P += 4
                    for dx, dy in directions:
                        ni = i + dx
                        nj = j + dy
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                         if (grid[ni][nj] == 1):
                            P = P - 1

        return P                    
def main():
        sol = Solution()
        tmp = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        result = sol.islandPerimeter(tmp)
        print(result)
if __name__ == "__main__":
        main()    
