class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)

def main():
    sol = Solution()
    result = sol.isSubsequence(s = "abc", t = "ahbgdc")
    print(result)
if __name__ == "__main__":
    main()