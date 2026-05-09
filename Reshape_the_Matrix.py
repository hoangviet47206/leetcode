class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n =len(mat[0])
        
        if ( (m * n) != (r * c)): return mat
        nums = []
        for i in range(m):
           for j in range(n):
              nums.append(mat[i][j])

        result = []
        inx = 0;
        for i in range(r):
            rev = []
            for j in range(c):
             rev.append(nums[inx])
             inx += 1

            result.append(rev)
        return result     
def main():
   sol = Solution()
   mat = [[1,2],[3,4]]
   result = sol.matrixReshape(mat, 1, 4)
   print(result)
if __name__ == "__main__":
   main()