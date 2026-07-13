class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in image:
            char = list()
            for j in range(len(i) -1, -1, -1):
                c = i[j]
                if c == 0:
                    c = 1
                else:
                    c = 0
                char.append(c)
            result.append(char)
        return result

def main():
    sol = Solution()

    image = [[1,1,0],[1,0,1],[0,0,0]]
    result = sol.flipAndInvertImage(image)

    print("Input:")
    for row in image:
        print(row)

    print("\nOutput:")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()


                    
                
