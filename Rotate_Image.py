class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(0, n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
              
def main():
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = sol.rotate(matrix)
    print(matrix)
if __name__ == "__main__":
    main()
    