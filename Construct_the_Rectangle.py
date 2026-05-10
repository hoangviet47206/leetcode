from math import sqrt

class Solution(object):
    def constructRectangle(self, area):
        rev = []

        for i in range(1, int(sqrt(area)) + 1):
            if area % i == 0:
                a = max(area // i, i)
                b = [a, area // a]
                rev.append(b)

        return rev[len(rev) - 1]

def main():
    sol = Solution()
    area = 4
    result = sol.constructRectangle(area)
    print(result)

if __name__ == "__main__":
    main()