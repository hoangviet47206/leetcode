class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        result = []
        for i in range(0, n):
            
            tmp = []
            for j in range(0, m):
                c = matrix[j][i]    
                tmp.append(c)

            result.append(tmp)


        return result        

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    sol = Solution()
    result = sol.transpose(matrix)

    print("Ma trận ban đầu:")
    for row in matrix:
        print(row)

    print("\nMa trận sau khi chuyển vị:")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()