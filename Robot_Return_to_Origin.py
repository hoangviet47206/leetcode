class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dem1, dem2 = 0, 0
        for i in range(len(moves)):
            ch = moves[i]
            if ch == 'R': dem1 += 1
            if ch == 'L': dem1 -= 1
            if ch == 'U': dem2 += 1
            if ch == 'D': dem2 -= 1
        return ((dem1 == 0) & (dem2 == 0))
def main():
    sol = Solution()
    moves = "UD"
    result = sol.judgeCircle(moves)
    print(result)
if __name__ == "__main__":
    main()