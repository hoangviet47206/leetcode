class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        if s == goal:
            return True

        for _ in range(len(s) - 1):
            tmp = ""
            for j in range(1, len(s)):
                tmp += s[j]

            tmp += s[0]

            if tmp == goal:
                return True

            s = tmp

        return False

def main():
    sol = Solution()
    s = "abcde"
    goal = "cedab"
    result = sol.rotateString(s, goal)
    print(result)
if __name__ == "__main__":
    main()