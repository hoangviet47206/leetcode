# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            areax = (right - left) * min(height(left), height[right])
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
            area = max(area, areax)
        
        return area
def main():
    sol = Solution()
    result = sol.maxArea( height = [1,8,6,2,5,4,8,3,7])
    print(result)
if __name__ == "__main__":
    main()    