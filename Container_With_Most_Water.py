# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        a = len(height)
        for i in range(0, a):
            for j in range(i + 1, a):
                areax = (j - i) * min(height[i], height[j])
                if (areax > area): area = areax
        
        return area
def main():
    sol = Solution()
    result = sol.maxArea( height = [1,8,6,2,5,4,8,3,7])
    print(result)
if __name__ == "__main__":
    main()    